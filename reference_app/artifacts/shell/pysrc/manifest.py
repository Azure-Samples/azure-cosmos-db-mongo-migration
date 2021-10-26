__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "October 2021"

import json
import os
import pprint
import sys
import time
import uuid

import arrow
import jinja2

from operator import itemgetter
from pysrc.config import Config


class Manifest(object):    

    def __init__(self):
        self.config = Config()
        try:
            infile = self.config.manifest_json_file()
            data   = self.load_json_file(infile)
            self.items = data['items']
            self.pipelines = data['pipeline_info']
        except:
            print('WARNING - NO MANIFEST JSON FILE')
            self.items = list()
            self.pipelines = list()

    def source_database_names(self):
        uniques = dict()
        for item in self.items:
            db = item['source_db']
            uniques[db] = 0
        return sorted(uniques.keys())

    def target_database_names(self):
        uniques = dict()
        for item in self.items:
            db = item['target_db']
            uniques[db] = 0
        return sorted(uniques.keys())

    def storage_container_names(self):
        uniques = dict()
        for item in self.items:
            raw = item['raw_storage_container']
            adf = item['adf_storage_container']
            uniques[raw] = 0
            uniques[adf] = 0
        return sorted(uniques.keys())

    def storage_container_names_for_source_db(self, dbname):
        uniques = dict()
        for item in self.items:
            if item['source_db'] == dbname:
                raw = item['raw_storage_container']
                adf = item['adf_storage_container']
                uniques[raw] = 0
                uniques[adf] = 0
        return sorted(uniques.keys())

    def adf_blob_datasets(self):
        datasets = dict()
        for item in self.items:
            name = item['adf_blob_dataset_name']
            datasets[name] = item['adf_storage_container']
        return datasets

    def cosmos_target_datasets(self):
        datasets = dict()
        for item in self.items:
            name = item['adf_cosmos_dataset_name']
            target_db = item['target_db']
            target_coll = item['target_coll']
            info = dict()
            info['dataset_name'] = name
            info['target_db']    = target_db
            info['target_coll']  = target_coll
            info['linked_svc']   = self.config.cosmos_linked_service_name(target_db)
            datasets[name] = info
        return datasets

    def items_for_source_db(self, source_db):
        db_items = list()
        for item in self.items:
            if item['source_db'] == source_db:
                db_items.append(item)
        return db_items

    def wrangle_script_names_for_source_db(self, source_db):
        uniques = dict()
        for item in self.items:
            if item['source_db'] == source_db:
                script = item['wrangle_script_name']
                uniques[script] = 0
        return sorted(uniques.keys())

    def cosmos_source_db_coll_tuples(self):
        uniques, tuples = dict(), list()
        for item in self.items:
            key = '{}:{}'.format(item['source_db'], item['source_coll'])
            uniques[key] = ( item['source_db'], item['source_coll'] )
        for key in sorted(uniques.keys()):
            tuples.append(uniques[key])
        return tuples

    def cosmos_target_db_coll_tuples(self):
        uniques, tuples = dict(), list()
        for item in self.items:
            key = '{}:{}'.format(item['target_db'], item['target_coll'])
            uniques[key] = ( item['target_db'], item['target_coll'] )
        for key in sorted(uniques.keys()):
            tuples.append(uniques[key])
        return tuples

    def cosmos_target_db_coll_tuples_for_source_db(self, source_db):
        uniques, tuples = dict(), list()
        for item in self.items:
            if item['source_db'] == source_db:
                key = '{}:{}'.format(item['target_db'], item['target_coll'])
                uniques[key] = ( item['target_db'], item['target_coll'] )
        for key in sorted(uniques.keys()):
            tuples.append(uniques[key])
        return tuples

    def cosmos_mapping_tuples(self):
        uniques, tuples = dict(), list()
        for item in self.items:
            key = '{}:{}:{}:{}'.format(
                item['source_db'], item['source_coll'],
                item['target_db'], item['target_coll'])
            uniques[key] = (
                item['source_db'], item['source_coll'],
                item['target_db'], item['target_coll'])
        for key in sorted(uniques.keys()):
            tuples.append(uniques[key])
        return tuples

    def target_db_for_source_db(self, source_db):
        for item in self.items:
            if item['source_db'] == source_db:
                return item['target_db']
        return None

    def collection_names_for_target_db(self, target_db):
        uniques = dict()
        for item in self.items:
            if item['target_db'] == target_db:
                coll = item['target_coll']
                uniques[coll] = 0
        return sorted(uniques.keys())

    def pk_for_container(self, target_db, target_coll):
        for item in self.items:
            if item['target_db'] == target_db:
                if item['target_coll'] == target_coll:
                    return item['partition_key']
        return None
 
    def get_merged_pipelines(self):
        pipelines_list = list()
        for pipeline in self.pipelines:
            pipeline_info = dict()
            pipeline_info['name'] = pipeline['name']
            pipeline_info['activities'] = list()
            prev_activity_name = ''
            uniques = dict()
            pipeline_items = pipeline['items']
            for item in pipeline_items:
                input_dataset = item['input_dataset']
                output_dataset = item['output_dataset']
                key = '{}:{}'.format(input_dataset, output_dataset)
                uniques[key] = 0
            activity_count = len(uniques.keys())
            activity_last_idx = activity_count - 1
            for idx, key in enumerate(sorted(uniques.keys())):
                tokens = key.split(':')
                input_dataset  = tokens[0]
                output_dataset = tokens[1]
                activity = dict()
                activity['name'] = 'copy_{}'.format(input_dataset)
                activity['input_dataset'] = input_dataset
                activity['output_dataset'] = output_dataset
                activity['has_dependency'] = len(prev_activity_name) > 0
                activity['dependent_activity'] = str(prev_activity_name)
                if idx < activity_last_idx:
                    activity['activity_sep'] = ','
                else:
                   activity['activity_sep'] = ''
                pipeline_info['activities'].append(activity)
                prev_activity_name = str(activity['name'])
            pipelines_list.append(pipeline_info)
        return pipelines_list

    def load_json_file(self, infile):
        with open(infile) as json_file:
            return json.load(json_file)

    def read_migrated_databases_list_file(self):
        infile = self.config.migrated_databases_list_file()
        databases = list()
        with open(infile, 'rt') as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith('#'):
                    pass
                else:
                    if len(stripped) > 0:
                        databases.append(stripped)
        return databases

    def write_obj_as_json_file(self, outfile, obj):
        txt = json.dumps(obj, sort_keys=False, indent=2)
        with open(outfile, 'wt') as f:
            f.write(txt)
        print("file written: " + outfile)
