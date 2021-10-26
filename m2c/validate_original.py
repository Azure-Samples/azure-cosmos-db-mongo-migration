"""
Usage:
    source env.sh ; python validate.py storage_containers
    source env.sh ; python validate.py raw_blobs
    source env.sh ; python validate.py wrangled_blobs
    source env.sh ; python validate.py target_cosmos_db
    source env.sh ; python validate.py all
"""

__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "July 2021"

import json
import os
import subprocess
import sys
import traceback
import uuid

from docopt import docopt
from operator import itemgetter
from pymongo import MongoClient

from pysrc.config import Config
from pysrc.manifest import Manifest
from storage import StorageUtil


class Validator(object):

    def __init__(self, args):
        self.args = args
        self.config = Config()
        self.manifest = Manifest()
        self.stor = StorageUtil()
        self.verbose = False
        for arg in args:
            if arg == '--verbose':
                self.verbose = True
        self.blob_data = dict()

    def validate_storage_containers(self):
        print('')
        print('validate_storage_containers ...')
        actual_container_names = dict()
        actual_containers = self.stor.list_containers()
        for actual in actual_containers:
            name = actual['name']
            actual_container_names[name] = actual

        for expected_cname in self.manifest.storage_container_names():
            if expected_cname in actual_container_names.keys():
                print('OK, container present: {}'.format(expected_cname))
            else:
                print('ERROR, container absent: {}'.format(expected_cname))

    def validate_raw_blobs(self):
        print('')
        print('validate_raw_blobs ...')
        for item in self.manifest.items:
            container = item["raw_storage_container"]
            blob_name = item["blob_name"]
            try:
                properties = self.stor.blob_properties(container, blob_name)
                size = int(properties['size'])
                key = 'raw:{}'.format(blob_name)
                self.blob_data[key] = size
                print('OK, raw blob present; container: {} blob: {} size: {}'.format(
                    container, blob_name, size))
            except:
                print('ERROR, raw blob absent: {} {}'.format(container, blob_name))

    def validate_wrangled_blobs(self):
        print('')
        print('validate_wrangled_blobs ...')
        for item in self.manifest.items:
            container = item["adf_storage_container"]
            raw_blob_name = item["blob_name"]
            adf_blob_name = item["wrangled_blob_name"]
            raw_key = 'raw:{}'.format(raw_blob_name)
            adf_key = 'adf:{}'.format(adf_blob_name)
            try:
                properties = self.stor.blob_properties(container, adf_blob_name)
                adf_size = int(properties['size'])
                self.blob_data[adf_key] = adf_size

                if raw_key in self.blob_data.keys():
                    raw_size = self.blob_data[raw_key]
                    ratio = float(adf_size) / float(raw_size)
                    print('OK, blob present; container: {} blob: {} size: {} adf/raw size ratio: {}'.format(
                        container, adf_blob_name, adf_size, ratio))
                else:
                    print('OK, blob present; container: {} blob: {} size: {}'.format(
                        container, adf_blob_name, adf_size))
            except:
                self.print_exception()
                print('ERROR, blob absent: {} {}'.format(container, adf_blob_name))

    def validate_target_cosmos_db(self):
        print('')
        print('validate_target_cosmos_db ...')
        conn_str = os.environ['M2C_COSMOS_MONGO_CONN_STRING']
        client = None
        try:
            client = MongoClient(conn_str)
        except:
            pass
        if client != None:
            print('OK, MongoClient created')
        else:
            print('ERROR, unable to create MongoClient from M2C_COSMOS_MONGO_CONN_STRING')
            return

        curr_dbname, curr_cname = None, None
        for db_coll_tuple in self.manifest.cosmos_target_db_coll_tuples():
            try:
                curr_dbname = db_coll_tuple[0]
                curr_cname  = db_coll_tuple[1]
                db_obj      = client[curr_dbname]
                db_colls    = db_obj.list_collection_names()
                if curr_cname in db_colls:
                    print("OK, collection '{}' is in database '{}'".format(
                        curr_cname, curr_dbname))
                    coll_obj = db_obj[curr_cname]
                    #cmd = { 'collStats' : curr_cname, 'verbose' : True }
                    stats = db_obj.command( { 'collStats' : curr_cname, 'verbose' : True })
                    if stats == None:
                        print("ERROR, can't get stats for collection '{}'".format(curr_cname))   
                    else:
                        print("OK, collection '{}' has {} documents".format(curr_cname, stats['count']))
                else:
                    print("ERROR, collection '{}' is NOT in database '{}'".format(
                        curr_cname, curr_dbname))
            except:
                print_exception('ERROR, exception on database: {} collection: {}'.format(
                    curr_cname, curr_dbname))
       
    def print_exception(self, msg=None):
        print('*** exception in storage.py - {}'.format(msg))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("*** traceback:")
        traceback.print_tb(exc_traceback, limit=2, file=sys.stderr)
        print("*** exception:")
        traceback.print_exception(
            exc_type, exc_value, exc_traceback, limit=2, file=sys.stderr)

def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version=__version__)
    print(arguments)


if __name__ == "__main__":
    #print(sys.argv)
    if len(sys.argv) > 1:
        func = sys.argv[1].lower()
        validator = Validator(sys.argv)

        if func == 'all':
            print('')
            print('validating all ...')
            validator.validate_storage_containers()
            validator.validate_raw_blobs()
            validator.validate_wrangled_blobs()
            validator.validate_target_cosmos_db()

        elif func == 'storage_containers':
            validator.validate_storage_containers()

        elif func == 'raw_blobs':
            validator.validate_raw_blobs()

        elif func == 'wrangled_blobs':
            validator.validate_wrangled_blobs()

        elif func == 'target_cosmos_db':
            validator.validate_target_cosmos_db()
        else:
            print_options('Error: invalid function: {}'.format(func))
    else:
            print_options('Error: no command-line args entered')
