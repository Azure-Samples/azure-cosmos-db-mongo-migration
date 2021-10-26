__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "October 2021"

import glob
import json
import os
import sys
import traceback
import uuid

from operator import itemgetter

from pysrc.config import Config

# Class StandardMappingGenerator implements the "built-in" data mapping
# generator.  It addresses the olympics and openflights reference databases
# but otherwise creates generic mappings.

class StandardMappingGenerator(object):

    def __init__(self, dbname):
        self.dbname = dbname
        self.config = Config()
        self.infile = self.config.db_metadata_file(self.dbname)
        self.metadata = self.load_json_file(self.infile)

    def generate(self):
        data = dict()
        data['source_dbname'] = self.dbname
        data['default_target_dbname'] = self.dbname
        
        if self.dbname == 'olympics':
            data['default_target_dbname'] = 'olympics'
            data['cosmos_db_autoscale_ru'] = 10000

        elif self.dbname == 'openflights':
            data['default_target_dbname'] = 'travel'
            data['cosmos_db_autoscale_ru'] = 5000

        coll_data = list()

        for coll in self.metadata['collections']:
            coll_info = dict()
            coll_info['name'] = coll['name']
            # create the intitial mapping dict, but customize below
            mapping = dict()
            mapping['target_dbname'] = data['default_target_dbname']
            mapping['target_container'] = coll['name']
            mapping['wrangling_algorithm'] = 'standard' 
            mapping['pk_name']  = 'pk' 
            mapping['pk_logic'] = list()
            mapping['pk_sep']  = '-' 
            mapping['doctype_name']  = 'doctype' 
            mapping['doctype_logic'] = list()
            mapping['doctype_sep']  = '-' 
            mapping['additions'] = list()
            mapping['excludes'] = list()

            if self.dbname == 'olympics':
                self.customize_olympics_mapping(mapping)
            if self.dbname == 'openflights':
                self.customize_openflights_mapping(mapping)

            coll_info['mapping'] = mapping
            coll_data.append(coll_info)

        data['collections'] = sorted(coll_data, key = itemgetter('name'))

        jstr = json.dumps(data, sort_keys=False, indent=2)
        outfile = self.config.db_mapping_file(self.dbname)
        self.write(outfile, jstr)

    def customize_olympics_mapping(self, mapping):
        cname = mapping['target_container']

        if cname == 'games':
            mapping['target_container'] = 'locations'
            mapping['pk_logic'] = [ ['attribute', 'games'] ]

        if cname == 'countries':
            mapping['target_container'] = 'locations'
            mapping['pk_logic'] =  [ ['attribute', 'NOC'] ]

        if 'summer' in cname:
            mapping['target_container'] = 'games'
            mapping['pk_logic'] = [ ['attribute', 'games'] ]
            mapping['doctype_logic'] = [ ['dynamic', 'source_cname'] ]

        if 'winter' in cname:
            mapping['target_container'] = 'games'
            mapping['pk_logic'] = [ ['attribute', 'games'] ]
            mapping['doctype_logic'] = [ ['dynamic', 'source_cname'] ]
            
        mapping['excludes'].append("id")

        mapping['additions'] = [
            ['dynamic', 'some_id', 'uuid'],
        ] 

    def customize_openflights_mapping(self, mapping):
        cname = mapping['target_container']

        if cname == 'routes':
            mapping['pk_logic'] = [ ['attribute', 'airline_id'] ] 
            mapping['doctype_logic'] = [ ['literal', 'route'] ] 
            mapping['additions'] = [
                ['dynamic', '_id', 'oid'],
                ['dynamic', 't', 'epoch']
            ] 
            mapping['excludes'].append('codeshare')
        else:
            mapping['pk_logic'] = [ ['attribute', 'name'] ] 

    def load_json_file(self, infile):
        with open(infile) as json_file:
            return json.load(json_file)

    def write_obj_as_json_file(self, outfile, obj):
        txt = json.dumps(obj, sort_keys=False, indent=2)
        with open(outfile, 'wt') as f:
            f.write(txt)
        print("file written: " + outfile)

    def write(self, outfile, s, verbose=True):
        with open(outfile, 'w') as f:
            f.write(s)
            if verbose:
                print('file written: {}'.format(outfile))
