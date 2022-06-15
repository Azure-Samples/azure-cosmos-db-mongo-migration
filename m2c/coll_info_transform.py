"""
Creates a JSON database metadata file from the output of 'db.getCollectionInfos()'
from the mongo shell.  Ad-hoc program as a workaround to extracting Atlas metadata.

Usage:
    python coll_info_transform.py transform_raw_coll_infos <dbname> <info-infile>
    python coll_info_transform.py transform_raw_coll_infos tmm tmp\tmm.json 
"""

__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "June 2022"

import json
import sys

import arrow


def transform_raw_coll_infos(dbname, infile):
    print('transform_raw_coll_infos, dbname: {}, infile: {}'.format(dbname, infile))
    root_obj = dict()
    collections = list()
    root_obj['dbname'] = dbname
    root_obj['utc_datetime'] =  str(arrow.utcnow())
    root_obj['collections'] = collections

    lines = read_lines(infile)
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('name:'):
            scrubbed = stripped.replace("\'",'').replace(',','')
            tokens = scrubbed.split()
            coll_name = tokens[1]
            coll_obj = dict()
            meta_obj = dict()
            coll_obj['name'] = coll_name
            coll_obj['metadata'] = meta_obj
            meta_obj['indexes'] = dict()
            meta_obj['doc_count'] = 1
            meta_obj['stats'] = dummy_stats(dbname, coll_name)
            collections.append(coll_obj)

    outfile = 'tmp/{}_metadata.json'.format(dbname)
    write_obj_as_json_file(outfile, root_obj)

def dummy_stats(dbname, coll_name):
    stats = dict()
    stats['ns'] = '{}.{}'.format(dbname, coll_name)
    stats['size'] = 1
    stats['count'] = 1
    stats['avgObjSize'] = 1
    stats['storageSize'] = 1
    stats['avgObjSize'] = 1
    stats['freeStorageSize'] = 1
    stats['capped'] = False
    stats['nindexes'] = 0
    stats['indexBuilds'] = list()
    stats['totalIndexSize'] = 1
    stats['totalSize'] = 1
    stats['indexSizes'] = dict()
    stats['scaleFactor'] = 1
    stats['ok'] = 1.0
    return stats

def read_lines(infile):
    lines = list()
    with open(infile, 'rt') as f:
        for line in f:
            lines.append(line)
    return lines

def load_json_file(infile):
    with open(infile) as json_file:
        return json.load(json_file)

def write_obj_as_json_file(outfile, obj, sort_keys=False):
    txt = json.dumps(obj, sort_keys=False, indent=2)
    with open(outfile, 'wt') as f:
        f.write(txt)
    print("file written: " + outfile)

def write(outfile, s, verbose=True):
    with open(outfile, 'w') as f:
        f.write(s)
        if verbose:
            print('file written: {}'.format(outfile))

def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version=__version__)
    print(arguments)


if __name__ == "__main__":
    #print(sys.argv)
    if len(sys.argv) > 1:
        func = sys.argv[1].lower()

        if func == 'transform_raw_coll_infos':
            dbname = sys.argv[2]
            infile = sys.argv[3]
            transform_raw_coll_infos(dbname, infile)
        else:
            print_options('Error: invalid function: {}'.format(func))
    else:
            print_options('Error: no command-line args entered')
