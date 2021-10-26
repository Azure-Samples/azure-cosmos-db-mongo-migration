"""
Usage:
    source env.sh ; python validate.py <function> <source_db> <outfile>
    source env.sh ; python validate.py storage_containers olympics tmp/vsc.json
    source env.sh ; python validate.py wrangled_blobs     olympics tmp/vwb.json
    source env.sh ; python validate.py target_cosmos_db   olympics tmp/vcdb.json
    source env.sh ; python validate.py all olympics 
"""

__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "October 2021"

import json
import os
import subprocess
import sys
import traceback
import uuid

import arrow

from docopt import docopt
from operator import itemgetter
from pymongo import MongoClient

from pysrc.config import Config
from pysrc.manifest import Manifest
from storage import StorageUtil


class OmniscriptValidator(object):

    def __init__(self, args, dbname, outfile):
        self.args = args
        self.dbname = dbname    # the source database name
        self.outfile = outfile  # write this file if validation is successful
        self.errfile = '{}.errors.json'.format(self.outfile) 
        self.config = Config()
        self.manifest = Manifest()
        self.stor = StorageUtil()
        self.verbose = False
        for arg in args:
            if arg == '--verbose':
                self.verbose = True
        self.blob_data = dict()

    def validate_storage_containers(self):
        self.initialize_outdata()
        self.outdata['function'] = 'storage_containers' 
        actual_container_names = dict()
        actual_containers = self.stor.list_containers()
        for actual in actual_containers:
            name = actual['name']
            actual_container_names[name] = actual

        expected_containers = self.manifest.storage_container_names_for_source_db(self.dbname)
        self.outdata['expected_containers'] = expected_containers
        self.outdata['actual_containers'] = sorted(actual_container_names.keys())

        for expected_cname in expected_containers:
            if expected_cname in actual_container_names.keys():
                msg = 'OK, container present: {}'.format(expected_cname)
                self.add_message(msg)
            else:
                msg = 'ERROR, container absent: {}'.format(expected_cname)
                self.add_error(msg)

        self.write_results_file()

    def validate_wrangled_blobs(self):
        self.initialize_outdata()
        self.outdata['function'] = 'wrangled_blobs' 
        for item in self.manifest.items:
            if item['source_db'] == self.dbname:
                container = item["adf_storage_container"]
                blob_name = item["wrangled_blob_name"]
                try:
                    properties = self.stor.blob_properties(container, blob_name)
                    #print(properties)
                    adf_size = int(properties['size'])
                    msg = 'OK, blob present; container: {} blob: {} size: {}'.format(
                        container, blob_name, adf_size)
                    self.add_message(msg)
                except:
                    msg = 'ERROR, blob absent: {} {}'.format(container, blob_name)
                    self.add_error(msg)
                    self.print_exception()

        self.write_results_file()

    def validate_target_cosmos_db(self):
        self.initialize_outdata()
        self.outdata['function'] = 'target_cosmos_db' 
        conn_str = os.environ['M2C_COSMOS_MONGO_CONN_STRING']
        client = None
        try:
            client = MongoClient(conn_str)
        except:
            self.add_error('ERROR, execption on creating MongoClient object')

        if client != None:
            self.add_message('OK, MongoClient created')
        else:
            self.add_error('ERROR, unable to create MongoClient from M2C_COSMOS_MONGO_CONN_STRING')
            return

        curr_dbname, curr_cname = None, None
        for db_coll_tuple in self.manifest.cosmos_target_db_coll_tuples_for_source_db(self.dbname):
            try:
                print(db_coll_tuple)
                curr_dbname = db_coll_tuple[0]
                curr_cname  = db_coll_tuple[1]
                db_obj      = client[curr_dbname]
                db_colls    = db_obj.list_collection_names()
                if curr_cname in db_colls:
                    msg = "OK, collection '{}' is in database '{}'".format(curr_cname, curr_dbname)
                    self.add_message(msg)
                    coll_obj = db_obj[curr_cname]
                    stats = db_obj.command( { 'collStats' : curr_cname, 'verbose' : True })
                    if stats == None:
                        msg = "ERROR, can't get stats for collection '{}'".format(curr_cname)
                        self.add_error(msg)
                    else:
                        msg = "OK, collection '{}' has {} documents".format(curr_cname, stats['count'])
                        self.add_message(msg)
                else:
                    msg = "ERROR, collection '{}' is NOT in database '{}'".format(curr_cname, curr_dbname)
                    self.add_error(msg)
            except:
                msg = 'ERROR, exception on database: {} collection: {}'.format(curr_dbname, curr_cname)
                self.add_error(msg)

        self.write_results_file()

    def validate_all(self):
        self.outfile = "tmp/validate_storage_containers.json"
        self.errfile = '{}.errors.json'.format(self.outfile)
        self.validate_storage_containers()

        self.outfile = "tmp/validate_wrangled_blobs.json"
        self.errfile = '{}.errors.json'.format(self.outfile)
        self.validate_wrangled_blobs()

        self.outfile = "tmp/validate_target_cosmos_db.json"
        self.errfile = '{}.errors.json'.format(self.outfile)
        self.validate_target_cosmos_db()

    def print_exception(self, msg=None):
        print('*** exception in storage.py - {}'.format(msg))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("*** traceback:")
        traceback.print_tb(exc_traceback, limit=2, file=sys.stderr)
        print("*** exception:")
        traceback.print_exception(
            exc_type, exc_value, exc_traceback, limit=2, file=sys.stderr)

    def initialize_outdata(self):
        self.outdata = dict()  # outdata is written as JSON as end of process
        self.outdata['dbname'] = self.dbname 
        self.outdata['outfile'] = self.outfile 
        self.outdata['timestamp'] = arrow.utcnow().format('YYYY-MM-DD HH:mm:ss UTC')
        self.outdata['messages'] = list()
        self.outdata['errors'] = list()

    def add_message(self, msg):
        self.outdata['messages'].append(msg)

    def has_messages(self):
        return len(self.outdata['messages']) > 0

    def add_error(self, msg):
        self.outdata['errors'].append(msg)

    def has_errors(self):
        return len(self.outdata['errors']) > 0

    def write_results_file(self):
        print(json.dumps(self.outdata, sort_keys=False, indent=2))
        if self.has_errors():
            print('OmniscriptValidator - validation errors encountered')
            self.write_obj_as_json_file(self.errfile, self.outdata)
        else:
            print('OmniscriptValidator - validation ok')
            self.write_obj_as_json_file(self.outfile, self.outdata)

    def write_obj_as_json_file(self, outfile, obj):
        txt = json.dumps(obj, sort_keys=False, indent=2)
        with open(outfile, 'wt') as f:
            f.write(txt)
        print("file written: " + outfile)

def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version=__version__)
    print(arguments)


if __name__ == "__main__":
    #print(sys.argv)

    if len(sys.argv) > 2:
        func = sys.argv[1].lower()
        dbname = sys.argv[2]
        outfile = 'none'
        if len(sys.argv) > 3:
            outfile = sys.argv[3]
        validator = OmniscriptValidator(sys.argv, dbname, outfile)

        if func == 'storage_containers':
            validator.validate_storage_containers()

        elif func == 'wrangled_blobs':
            validator.validate_wrangled_blobs()

        elif func == 'target_cosmos_db':
            validator.validate_target_cosmos_db()

        elif func == 'all':
            validator.validate_all()

        else:
            print_options('Error: invalid function: {}'.format(func))
    else:
            print_options('Error: no command-line args entered')
