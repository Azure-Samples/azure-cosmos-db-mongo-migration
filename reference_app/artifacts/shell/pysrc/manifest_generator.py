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

# This class generates the similar "manifest" csv and json files, which
# weave together the extracted metadata from the source databases, as well
# as the used-edited mapping files.  The manifest is thus a complete and
# correlated list of all databases, collections, blobs, etc. in the migration .
# process.  The manifest is used to generate various artifacts - code, scripts,
# and Excel reporting. 

class ManifestGenerator(object):    

    def __init__(self):
        self.config = Config()

    def generate_manifest_files(self):
        databases_list = self.read_migrated_databases_list_file()
        print('databases_list: {}'.format(databases_list))
        manifest_rows = list()
        columns = list()
        columns.append('Source DB')
        columns.append('Source Coll')
        columns.append('Doc Count')
        columns.append('Avg Doc Size')
        columns.append('Target DB')
        columns.append('Target Coll')
        columns.append('Partition Key')
        columns.append('Blob Name')
        columns.append('Raw Storage Container')
        columns.append('ADF Storage Container')
        columns.append('ADF Blob Doc Count')
        columns.append('ADF Blob Dataset Name')
        columns.append('ADF Cosmos Dataset Name')
        columns.append('ADF Pipeline Name')
        manifest_rows.append(','.join(columns))

        for source_db in sorted(databases_list):
            mappings = self.load_json_file(self.config.db_mapping_file(source_db))
            metadata = self.load_json_file(self.config.db_metadata_file(source_db))

            for coll in sorted(mappings['collections'], key = itemgetter('name')):
                source_coll = coll['name']
                target_db   = coll['mapping']['target_dbname']
                target_coll = coll['mapping']['target_container']
                pk_name     = coll['mapping']['pk_name']
                doc_count   = self.doc_count(metadata, source_coll)
                doc_size    = self.avg_doc_size(metadata, source_coll)
                blob_name          = self.config.blob_name(source_db, source_coll)
                raw_blob_container = self.config.blob_raw_container_name(source_db)
                adf_blob_container = self.config.blob_adf_container_name(target_db, target_coll)
                adf_blob_dataset   = self.config.blob_dataset_name(target_db, target_coll)
                adf_cosmos_dataset = self.config.cosmos_dataset_name(target_db, target_coll)
                adf_pipeline       = self.config.adf_pipeline_name(target_db, target_coll) 

                row = '{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(
                    source_db,
                    source_coll,
                    doc_count,
                    doc_size,
                    target_db,
                    target_coll,
                    pk_name,
                    blob_name,
                    raw_blob_container,
                    adf_blob_container,
                    -1,
                    adf_blob_dataset,
                    adf_cosmos_dataset,
                    adf_pipeline)
                manifest_rows.append(row)

        # Save the manifest CSV/Excel file
        self.write(self.config.manifest_csv_file(), "\n".join(manifest_rows))

        # Also save the augmented manifest JSON file
        self.save_manifest_as_json(columns, manifest_rows)

    def save_manifest_as_json(self, columns, manifest_rows):
        manifest, items = dict(), list()
        manifest['generated_on'] = self.config.timestamp()
        manifest['items'] = items

        for row_idx, row in enumerate(manifest_rows):
            if row_idx > 0:
                item = dict()
                values = row.split(',')
                for idx, value in enumerate(values):
                    attr_name = columns[idx].lower().replace(' ', '_').strip()
                    item[attr_name] = value

                source_db   = item['source_db']
                source_coll = item['source_coll']
                target_db   = item['target_db']
                target_coll = item['target_coll']

                wrangled_outfile = self.config.wrangled_outfile(source_db, source_coll)

                item['mongoexports_dir']    = self.config.mongoexports_dir(source_db)
                item['mongoexport_file']    = self.config.mongoexport_file(source_db, source_coll)
                item['wrangle_script_name'] = self.config.wrangle_script_name(source_db, source_coll)
                item['wrangled_outfile']    = wrangled_outfile
                item['wrangled_blob_name']  = os.path.basename(wrangled_outfile)
                item['local_file_path']     = self.config.wrangling_blob_download_file(source_db, source_coll)
                items.append(item)

        manifest['pipeline_info'] = self.collect_pipelines(columns, items)
        self.write_obj_as_json_file(self.config.manifest_json_file(), manifest)

    def collect_pipelines(self, columns, manifest_items):
        # first identify the unique pipeline names
        unique_pipeline_names = dict()
        for item in manifest_items:
            name = item['adf_pipeline_name']
            if name not in columns:
                unique_pipeline_names[name] = 0

        # next collect the info/copies for each pipeline
        pipelines = list()
        for pipeline_name in sorted(unique_pipeline_names.keys()):
            pipeline, pipeline_items = dict(), list()
            pipeline['name']  = pipeline_name
            pipeline['items'] = pipeline_items
            pipelines.append(pipeline)

            for item in manifest_items:
                name = item['adf_pipeline_name']
                if name == pipeline_name:
                    source_db   = item['source_db']
                    source_coll = item['source_coll']
                    target_db   = item['target_db']
                    target_coll = item['target_coll']
                    info = dict()
                    info['input_dataset'] = item['adf_blob_dataset_name']
                    info['output_dataset'] = item['adf_cosmos_dataset_name']
                    info['source'] = '{}:{}'.format(source_db, source_coll)
                    info['target'] = '{}:{}'.format(target_db, target_coll)
                    info['source_linked_svc'] = self.config.blob_linked_service_name()
                    info['target_linked_svc'] = self.config.cosmos_linked_service_name(target_db)
                    pipeline_items.append(info)

        return pipelines

    def doc_count(self, metadata, coll_name):
        try:
            for coll in metadata['collections']:
                if coll['name'] == coll_name:
                    return coll['metadata']['stats']['count']
            return -1
        except:
            return -1

    def avg_doc_size(self, metadata, coll_name):
        try:
            for coll in metadata['collections']:
                if coll['name'] == coll_name:
                    return coll['metadata']['stats']['avgObjSize']
            return -1
        except:
            return -1

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

    def write(self, outfile, s, verbose=True):
        with open(outfile, 'w') as f:
            f.write(s)
            if verbose:
                print('file written: {}'.format(outfile))
