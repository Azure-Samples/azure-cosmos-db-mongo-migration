"""
This Python script reads a "source" mongoexport file and transforms it into
the format required for loading into the "target" database.

Usage:
    source env.sh ; python wrangle.py transform --db openflights --in-container openflights-raw --blobname openflights__airlines__source.json --out-container openflights-raw
"""

__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com,christopher.joakim@gmail.com"
__license__ = "MIT"
__version__ = "October 2021"

import json
import os
import pprint
import sys
import time
import traceback
import uuid

import arrow
from docopt import docopt
from os.path import abspath
from operator import itemgetter
from bson.objectid import ObjectId

from pysrc.config import Config
from pysrc.standard_doc_wrangler import StandardDocumentWrangler

from storage import StorageUtil


class Transformer(object):

    def __init__(self, args):
        self.start_time = time.time()
        self.args = args
        self.config = Config()
        self.stor = StorageUtil()
        self.infile = None
        self.status = 'constructor'
        self.elapsed_time = -1
        self.lines_processed = 0
        self.verbose = self.flag_arg('--verbose')

        self.dbname        = self.cli_arg('--db')
        self.source_coll   = self.cli_arg('--source-coll')
        self.in_container  = self.cli_arg('--in-container')
        self.blobname      = self.cli_arg('--blobname')
        self.filename      = self.cli_arg('--filename')
        self.infile        = self.cli_arg('--infile')
        self.outfile       = self.cli_arg('--outfile')
        self.out_container = self.cli_arg('--out-container')

        print('Transformer constructor; parsed args:')
        print('  dbname:        {}'.format(self.dbname))
        print('  source_coll:   {}'.format(self.source_coll))
        print('  in_container:  {}'.format(self.in_container))
        print('  blobname:      {}'.format(self.blobname))
        print('  filename:      {}'.format(self.filename))
        print('  infile:        {}'.format(self.infile))
        print('  outfile:       {}'.format(self.outfile))
        print('  out_container: {}'.format(self.out_container))

        self.mappings = self.load_container_mappings()
        print('mappings:')
        print(json.dumps(self.mappings, indent=2, sort_keys=False))

        # Configure wrangling logic
        self.doc_wrangler = StandardDocumentWrangler(self.mappings)
        self.wrangling_algorithm = self.mappings['mapping']['wrangling_algorithm'].strip().lower()
        print('wrangling_algorithm: {}'.format(self.wrangling_algorithm))
        self.pk_name = self.mappings['mapping']['pk_name'].strip().lower()
        self.pk_logic = self.mappings['mapping']['pk_logic']
        self.do_pk_wrangling = len(self.pk_name) > 0
        self.excludes = self.mappings['mapping']['excludes']
        self.do_excludes = len(self.excludes) > 0

    def transform_blob(self):
        # Fail fast if invalid inputs:
        if self.dbname == None:
            raise Exception("Error: no --db specified")
        if self.source_coll == None:
            raise Exception("Error: no --source-coll specified")
        if self.in_container == None:
            raise Exception("Error: no --in_container specified")
        if self.blobname == None:
            raise Exception("Error: no --blobname specified")
        if self.filename == None:
            raise Exception("Error: no --filename specified")
        if self.outfile == None:
            raise Exception("Error: no --outfile specified")
        if self.out_container == None:
            raise Exception("Error: no --out-container specified")
        if self.mappings == None:
            raise Exception("Error: mappings")

        self.download_blob()
        self.transform_downloaded_blob()
        self.upload_transformed_blob()
        self.elapsed_time = time.time() - self.start_time
        self.status = 'completed'

    def download_blob(self):
        print('download_blob {} from {} to {}'.format(
            self.blobname, self.in_container, self.filename))
        start = time.time()
        self.stor.download_blob(
            self.in_container, self.blobname, self.filename)
        elapsed = time.time() - start
        print('downloaded {} in {}ms'.format(self.filename, elapsed))

    def transform_downloaded_blob(self):
        start, line_count = time.time(), 0
        it = text_file_iterator(self.filename)  # use an iterator to handle huge files

        with open(self.outfile, 'wt') as out:
            for i, line in enumerate(it):
                line_count = line_count + 1
                if self.verbose:
                    print(line)
                doc = json.loads(line)
                self.doc_wrangler.wrangle(doc)
                out.write(json.dumps(doc, separators=(',', ':')))
                out.write("\n")
                self.lines_processed = self.lines_processed + 1

        elapsed = time.time() - start
        print('transformed {} lines in {}'.format(line_count, elapsed))

    def transform_file(self):
        # Fail fast if invalid inputs:
        if self.dbname == None:
            raise Exception("Error: no --db specified")
        if self.source_coll == None:
            raise Exception("Error: no --source-coll specified")
        if self.infile == None:
            raise Exception("Error: no --infile specified")
        if self.outfile == None:
            raise Exception("Error: no --outfile specified")
        if self.mappings == None:
            raise Exception("Error: mappings")

        start, line_count = time.time(), 0
        it = text_file_iterator(self.infile)  # use an iterator to handle huge files

        with open(self.outfile, 'wt') as out:
            for i, line in enumerate(it):
                line_count = line_count + 1
                if self.verbose:
                    print(line)
                doc = json.loads(line)
                self.doc_wrangler.wrangle(doc)
                out.write(json.dumps(doc, separators=(',', ':')))
                out.write("\n")
                self.lines_processed = self.lines_processed + 1

        self.elapsed_time = time.time() - self.start_time
        self.status = 'completed'
        print('transformed {} lines in {}'.format(line_count, self.elapsed_time))

    def upload_transformed_blob(self):
        bname = os.path.basename(self.outfile)
        start = time.time()
        print('uploading {} at {} to {}/{}'.format(
            self.filename, self.timestamp(), self.out_container, bname))
        self.stor.upload_blob(self.outfile, self.out_container, bname, overwrite=True)
        elapsed = time.time() - start
        print('uploaded {}/{} at {} in {}'.format(
            self.filename, bname, self.timestamp(), elapsed))

        properties = self.stor.blob_properties(self.out_container, bname)
        print(properties)

    def print_summary(self):
        print('-')
        print('SUMMARY for args:  {}'.format(" ".join(self.args))) 
        print('  status:          {}'.format(self.status)) 
        print('  lines_processed: {}'.format(self.lines_processed)) 
        print('  start_time:      {}'.format(self.start_time)) 
        print('  elapsed_time:    {}'.format(self.elapsed_time))

    def cli_arg(self, flag):
        for idx, arg in enumerate(self.args):
            if arg == flag:
                return args[idx + 1]
        return None

    def flag_arg(self, flag):
        for idx, arg in enumerate(self.args):
            if arg == flag:
                return True
        return False

    def timestamp(self):
        return arrow.utcnow().format('YYYY-MM-DD HH:mm:ss UTC')

    def is_successful(self):
        return self.status == 'successful'

    def load_container_mappings(self):
        cname = self.source_coll
        print('load_container_mappings; cname: {}'.format(cname))
        fname = '{}_mapping.json'.format(self.dbname)
        print('load_container_mappings; fname: {}'.format(fname))

        allmeta = self.load_json_file(fname)
        for mapping in allmeta['collections']:
            if mapping['name'] == cname:
                mapping['source_dbname'] = allmeta['source_dbname']
                mapping['default_target_dbname'] = allmeta['default_target_dbname']
                return mapping
        raise Exception("Error: container '{}' missing in metadata file {}".format(cname, fname))

    def parse_container_from_filename(self, filename):
        tokens = os.path.basename(filename).split('__')
        print('parse_container_from_filename tokens: {}'.format(tokens))
        return tokens[-2]

    def load_json_file(self, infile):
        with open(infile) as json_file:
            return json.load(json_file)

def text_file_iterator(infile):
    # return a line generator that can be iterated with iterate()
    # this is more efficient as the file is read line-by-line
    with open(infile, 'rt') as f:
        for line in f:
            yield line.strip()

def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version=__version__)
    print(arguments)

def get_program_args():
    # get the program args from either the command-line or the CLI_ARGS
    # environment variable if running in a Docker container.
    args = list()
    if len(sys.argv) > 1:
        args = sys.argv
    else:
        cli_arg_str = os.environ['CLI_ARGS']
        print('CLI_ARGS: {}'.format(cli_arg_str))
        args = cli_arg_str.split()
    return args


if __name__ == "__main__":
    args = get_program_args()
    print('__main__ args: {}'.format(args))
    if len(args) > 0:
        func = args[1].lower()
        print('func: {}'.format(func))
        if func == 'transform_blob':
            try:
                t = Transformer(args)
                t.transform_blob()
                t.print_summary()
            except:
                print("ERROR: TRANSFORMATION_FAILED for args {}".format(args))
                traceback.print_exc(file=sys.stdout)
        elif func == 'transform_file':
            try:
                t = Transformer(args)
                t.transform_file()
                t.print_summary()
            except:
                print("ERROR: TRANSFORMATION_FAILED for args {}".format(args))
                traceback.print_exc(file=sys.stdout)
        else:
            print_options('Error: invalid function: {}'.format(func))
    else:
            print_options('Error: no command-line args entered')
