"""
Usage:
    source env.sh ; python storage.py create_blob_container openflights-raw
    source env.sh ; python storage.py create_blob_container openflights-adf
    source env.sh ; python storage.py create_blob_container test
    source env.sh ; python storage.py delete_blob_container openflights-raw
    source env.sh ; python storage.py list_blob_containers
    source env.sh ; python storage.py list_blob_container openflights-raw
    source env.sh ; python storage.py upload_blob local_file_path cname blob_name
    source env.sh ; python storage.py upload_blob requirements.in test requirements.in
    source env.sh ; python storage.py download_blob test aaa.txt aaa-down.txt
"""

__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
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

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

from azure.core.exceptions import ResourceExistsError
from azure.core.exceptions import ResourceNotFoundError


class StorageUtil(object):

    def __init__(self):
        conn_str = os.environ['M2C_STORAGE_CONNECTION_STRING']
        self.blob_service_client = BlobServiceClient.from_connection_string(conn_str)

    def list_containers(self):
        try:
            return self.blob_service_client.list_containers()
            # a list of <class 'azure.storage.blob._models.ContainerProperties'>
        except:
            self.print_exception('list_containers, returning empty list')
            return list()

    def create_container(self, cname):
        try:
            container_client = self.blob_service_client.get_container_client(cname)
            container_client.create_container()
            print('create_container: {}'.format(cname))
        except:
            self.print_exception('create_container {}'.format(cname))

    def delete_container(self, cname):
        try:
            container_client = self.blob_service_client.get_container_client(cname)
            container_client.delete_container()
            print('delete_container: {}'.format(cname))
        except:
            self.print_exception('delete_container {}'.format(cname))

    def list_container(self, cname):
        try:
            container_client = self.blob_service_client.get_container_client(cname)
            return container_client.list_blobs()
        except:
            self.print_exception('list_container {}'.format(cname))
            return list()

    def upload_blob(self, local_file_path, cname, blob_name, overwrite=True):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=cname, blob=blob_name)
            with open(local_file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=overwrite)
            print('upload_blob: {} {} -> {} {}'.format(local_file_path, overwrite, cname, blob_name))
        except:
            msg = 'local_file_path: {}  cname: {}  blob_name: {}'.format(
                local_file_path, cname, blob_name)
            self.print_exception('upload_blob {}'.format(msg))

    def download_blob(self, cname, blob_name, local_file_path):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=cname, blob=blob_name)
            with open(local_file_path, "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())
            print('download_blob: {} {} -> {}'.format(cname, blob_name, local_file_path))
        except:
            msg = 'cname: {}  blob_name: {}  local_file_path: {}'.format(
                cname, blob_name, local_file_path)
            self.print_exception('download_blob {}'.format(msg))

    def blob_properties(self, cname, blob_name):
        try:
            blob_client = self.blob_service_client.get_blob_client(container=cname, blob=blob_name)
            return blob_client.get_blob_properties()
        except:
            self.print_exception('blob_properties {} {}'.format(cname, blob_name))

    def print_exception(self, msg=None):
        print('*** exception in storage.py - {}'.format(msg))
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print("*** traceback:")
        traceback.print_tb(exc_traceback, limit=2, file=sys.stderr)
        print("*** exception:")
        traceback.print_exception(
            exc_type, exc_value, exc_traceback, limit=2, file=sys.stderr)


def list_blob_containers():
    stor = StorageUtil()
    containers = stor.list_containers()
    count = 0
    for idx, c in enumerate(containers):
        count = count + 1
        # print(str(type(c))) # <class 'azure.storage.blob._models.ContainerProperties'>
        print('{} {}'.format(idx + 1, c.name))
    if count < 1:
        print('no containers')
        
def list_blob_container(cname):
    stor = StorageUtil()
    blobs = stor.list_container(cname)
    for idx, b in enumerate(blobs):
        #print(str(type(b))) # <class 'azure.storage.blob._models.BlobProperties'>
        print('{} {}'.format(idx + 1, b.name))

def create_blob_container(cname):
    print('create_blob_container; cname: {}'.format(cname))
    stor = StorageUtil()
    stor.create_container(cname)

def delete_blob_container(cname):
    print('delete_blob_container; cname: {}'.format(cname))
    stor = StorageUtil()
    stor.delete_container(cname)

def upload_blob(local_file_path, cname, blob_name):
    print('upload_blob; {} {} {}'.format(local_file_path, cname, blob_name))
    stor = StorageUtil()
    stor.upload_blob(local_file_path, cname, blob_name)

def download_blob(cname, blob_name, local_file_path):
    print('download_blob; {} {} {}'.format(cname, blob_name, local_file_path))
    stor = StorageUtil()
    stor.download_blob(cname, blob_name, local_file_path)

def load_json_file(infile):
    with open(infile) as json_file:
        return json.load(json_file)

def write_obj_as_json_file(outfile, obj):
    txt = json.dumps(obj, sort_keys=False, indent=2)
    with open(outfile, 'wt') as f:
        f.write(txt)
    print("file written: " + outfile)

def write(outfile, s, verbose=True):
    with open(outfile, 'w') as f:
        f.write(s)
        if verbose:
            print('file written: {}'.format(outfile))

def boolean_flag_arg(flag):
    for arg in sys.argv:
        if arg == flag:
            return True
    return False


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version=__version__)
    print(arguments)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        func = sys.argv[1].lower()

        if func == 'list_blob_containers':
            list_blob_containers()

        elif func == 'list_blob_container':
            cname = sys.argv[2]
            list_blob_container(cname)

        elif func == 'create_blob_container':
            cname = sys.argv[2]
            create_blob_container(cname)

        elif func == 'delete_blob_container':
            cname = sys.argv[2]
            delete_blob_container(cname)

        elif func == 'upload_blob':
            local_file_path = sys.argv[2]
            cname = sys.argv[3]
            if len(sys.argv) > 4:
                blob_name = sys.argv[4]
            else:
                blob_name = os.path.basename(local_file_path) 
            upload_blob(local_file_path, cname, blob_name)

        elif func == 'download_blob':
            cname = sys.argv[2]
            blob_name = sys.argv[3]
            local_file_path = sys.argv[4]
            skip_download = boolean_flag_arg('--skip-download')
            if skip_download == False:
                download_blob(cname, blob_name, local_file_path)
        else:
            print_options('Error: invalid function: {}'.format(func))
    else:
            print_options('Error: no command-line args entered')
