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
from pysrc.manifest import Manifest

# Class ArtifactGenerator is used to generate all script and code
# artifacts in this application, by using the extracted source database
# metadata as well as a customer-edited mapping file.

class ArtifactGenerator(object):    

    def __init__(self, dbname, mapping_data):
        self.dbname = dbname
        self.mapping_data = mapping_data
        if 'collections' in mapping_data.keys():
            self.collections = mapping_data['collections']
        else:
            self.collections = list()

        self.config = Config()
        self.manifest = None
        self.shell_type          = self.config.shell_type
        self.ssl                 = self.config.ssl
        self.artifact_types      = self.config.artifact_types
        self.artifacts_dir       = self.config.artifacts_dir
        self.shell_artifacts_dir = self.config.shell_artifacts_dir()
        self.mongo_artifacts_dir = self.config.mongo_artifacts_dir()
        self.mongoexports_dir    = self.config.mongoexports_dir(dbname)
        self.data_dir            = self.config.data_dir

    def get_manifest(self):
        if self.manifest == None:
            self.manifest = Manifest()
        return self.manifest

    def generate_initial_scripts(self):
        print('generate_initial_scripts') 
        databases_list = self.read_migrated_databases_list_file()
        print('databases_list: {}'.format(databases_list))

        template_data = dict()
        template_data['gen_timestamp'] = self.timestamp()
        template_data['gen_by'] = 'artifact_generator.py generate_initial_scripts()'
        template_data['databases'] = databases_list

        self.generate_extract_metadata_script(template_data)
        self.generate_generate_mapping_files_script(template_data)
        self.generate_generate_artifacts_script(template_data)

    def generate_extract_metadata_script(self, template_data):
        template_name = 'extract_metadata.txt'
        self.render_template(template_name, template_data, 'extract_metadata.sh')

    def generate_generate_mapping_files_script(self, template_data):
        template_name = 'generate_mapping_files.txt'
        self.render_template(template_name, template_data, 'generate_mapping_files.sh')

    def generate_generate_artifacts_script(self, template_data):
        template_name = 'generate_artifacts.txt'
        self.render_template(template_name, template_data, 'generate_artifacts.sh')

    def generate(self):
        if (self.gen_artifact('--mongoexports')):
            self.gen_mongoexports()

        if (self.gen_artifact('--create-containers')):
            self.gen_python_create_containers() 

        if (self.gen_artifact('--py-uploads')):
            self.gen_python_uploads() 

        if (self.gen_artifact('--az-login')):
            self.gen_az_login() 

        if (self.gen_artifact('--az-cli-uploads')):
            self.gen_az_cli_uploads() 

        if (self.gen_artifact('--wrangle-scripts-for-db')):
            self.gen_wrangle_scripts_for_db() 

        if (self.gen_artifact('--wrangle-scripts-individual')):
            self.gen_wrangle_scripts_individual() 

        if (self.gen_artifact('--migrate-db-omniscript')):
            self.gen_migrate_db_omniscript() 

        if (self.gen_artifact('--adf-linked-services')):
            self.gen_adf_linked_services() 

        if (self.gen_artifact('--adf-blob-datasets')):
            self.gen_adf_blob_datasets() 

        if (self.gen_artifact('--adf-cosmos-mongo-datasets')):
            self.gen_adf_cosmos_mongo_datasets() 

        if (self.gen_artifact('--adf-pipelines')):
            self.gen_adf_pipelines() 

        if (self.gen_artifact('--adf-az-pipeline-scripts')):
            self.gen_adf_az_pipeline_scripts() 

        if (self.gen_artifact('--target-cosmos-az-create')):
            self.gen_target_cosmos_az_create() 

        if (self.gen_artifact('--target-cosmos-mongo-indexes')):
            self.gen_target_cosmos_mongo_indexes() 

    def gen_artifact(self, name):
        if '--all' in self.artifact_types:
            return True
            
        if name == self.artifact_types:
            return True

        if '--simple' in self.artifact_types:
            if 'omniscript' in name:
                return False
            if '--adf' in name:
                return False
            if 'noblob' in self.artifact_types:
                if 'upload' in name:
                    return False
            return True

        return False

    # def gen_artifact(self, name):
    #     for arg in sys.argv:
    #         if arg == '--all':
    #             return True
    #         elif arg == name:
    #             return True 
    #     return False 

    def gen_mongoexports(self):
        template_name = 'mongoexport_script.txt'
        outfile = '{}/{}_mongoexports.sh'.format(self.shell_artifacts_dir, self.dbname)
        template_data = dict()
        template_data['dbname'] = self.dbname
        template_data['gen_timestamp'] = self.timestamp()
        template_data['gen_by'] = 'artifact_generator.py gen_mongoexports()'
        template_data['uri']  = self.config.source_mongodb_uri()
        template_data['url']  = self.config.source_mongodb_url
        template_data['host'] = self.config.source_mongodb_host 
        template_data['post'] = self.config.source_mongodb_port
        template_data['user'] = self.config.source_mongodb_user 
        template_data['pass'] = self.config.source_mongodb_pass
        template_data['ssl']  = ' # no --ssl' # self.config.source_mongodb_ssl 
        template_data['collections'] = self.collections
        template_data['outdir'] = self.mongoexports_dir
        self.render_template(template_name, template_data, outfile)

    def gen_python_create_containers(self):
        manifest = self.get_manifest()
        container_names = manifest.storage_container_names()
        template_name = 'create_blob_containers.txt'
        outfile = '{}/create_blob_containers.sh'.format(self.shell_artifacts_dir)
        template_data = dict()
        template_data['gen_timestamp'] = self.timestamp()
        template_data['gen_by'] = 'artifact_generator.py gen_python_create_containers()'
        template_data['container_names'] = container_names
        self.render_template(template_name, template_data, outfile)

        # also generate other files related to create_blob_containers and python
        for template_name in 'env.sh,pyenv.sh,storage.py,requirements.in,requirements.txt,venv.sh'.split(','):
            outfile = '{}/{}'.format(self.shell_artifacts_dir, template_name)
            self.render_template(template_name, template_data, outfile)

    def gen_python_uploads(self):
        mongoexports_dir = self.config.mongoexports_dir(self.dbname)
        template_name = 'blob_uploads_python.txt'
        outfile = '{}/{}_python_mongoexport_uploads.sh'.format(
            self.shell_artifacts_dir, self.dbname)
        template_data = dict()
        collection_data = list()
        template_data['dbname'] = self.dbname
        template_data['gen_timestamp'] = self.timestamp()
        template_data['gen_by'] = 'artifact_generator.py gen_python_uploads()'
        template_data['collections'] = collection_data
        template_data['container'] = self.config.blob_raw_container_name(self.dbname)

        for c in self.collections:
            cname = c['name']
            local_file = self.config.mongoexport_file(self.dbname, cname)
            coll_dict = dict()
            coll_dict['local_file_path'] = local_file
            coll_dict['blob_name'] = os.path.basename(local_file)
            collection_data.append(coll_dict)
        self.render_template(template_name, template_data, outfile)

    def gen_az_login(self):
        template_name = 'az_login_sp.txt'
        outfile = '{}/az_login_sp.sh'.format(self.shell_artifacts_dir)
        template_data = dict()
        template_data['gen_timestamp'] = self.timestamp()
        self.render_template(template_name, template_data, outfile)

    def gen_az_cli_uploads(self):
        mongoexports_dir = self.config.mongoexports_dir(self.dbname)
        template_name = 'blob_uploads_az_cli.txt'
        outfile = '{}/{}_az_cli_mongoexport_uploads.sh'.format(
            self.shell_artifacts_dir, self.dbname)
        template_data = dict()
        collection_data = list()
        template_data['dbname'] = self.dbname
        template_data['gen_timestamp'] = self.timestamp()
        template_data['gen_by'] = 'artifact_generator.py gen_az_cli_uploads()'
        template_data['collections'] = collection_data
        template_data['container'] = self.config.blob_raw_container_name(self.dbname)

        for c in self.collections:
            cname = c['name']
            local_file = self.config.mongoexport_file(self.dbname, cname)
            coll_dict = dict()
            coll_dict['local_file_path'] = local_file
            coll_dict['blob_name'] = os.path.basename(local_file)
            collection_data.append(coll_dict)
        
        self.render_template(template_name, template_data, outfile)

    def gen_wrangle_scripts_for_db(self):
        manifest = self.get_manifest()
        script_names = manifest.wrangle_script_names_for_source_db(self.dbname)
        mongoexports_dir = self.config.mongoexports_dir(self.dbname)
        template_name = 'wrangle_all.txt'
        outfile = '{}/wrangle_{}_all.sh'.format(self.shell_artifacts_dir, self.dbname)
        template_data = dict()
        collection_data = list()
        template_data['dbname'] = self.dbname
        template_data['gen_timestamp'] = self.timestamp()
        template_data['gen_by'] = 'artifact_generator.py gen_wrangle_scripts_for_db()'
        template_data['script_names'] = script_names
        self.render_template(template_name, template_data, outfile)

    def gen_wrangle_scripts_individual(self):
        manifest = self.get_manifest()
        mongoexports_dir = self.config.mongoexports_dir(self.dbname)

        # Use one of three jinja2 templates
        template_name = 'wrangle_one_blob.txt'
        if 'noblob' in self.artifact_types:
            if 'verbatim' in self.artifact_types:
                template_name = 'wrangle_one_file_verbatim.txt'
            else:
                template_name = 'wrangle_one_file.txt'

        items = manifest.items_for_source_db(self.dbname)
        for item in items:
            #print(item)
            template_data = dict()
            collection_data = list()
            template_data['dbname'] = self.dbname
            template_data['gen_timestamp'] = self.timestamp()
            template_data['gen_by'] = 'artifact_generator.py gen_wrangle_scripts_individual()'
            template_data['container'] = self.config.blob_raw_container_name(self.dbname)

            blob_name = item['blob_name']
            wrangle_script_name = item['wrangle_script_name']
            outfile = '{}/{}'.format(
                self.shell_artifacts_dir, wrangle_script_name)
            redirect = 'out/{}/wrangle_{}.out'.format(self.dbname, wrangle_script_name)

            template_data['raw_storage_container'] = item['raw_storage_container']
            template_data['adf_storage_container'] = item['adf_storage_container']
            template_data['source_coll'] = item['source_coll']
            template_data['blob_name'] = blob_name

            # TODO - should be:
            # --filename tmp/openflights/openflights__planes.json \
            #local_file = self.config.mongoexport_file(self.dbname, item['source_coll'])
            template_data['local_file_path'] = item['local_file_path']

            template_data['wrangled_outfile'] = item['wrangled_outfile']

            infile = '{}/{}__{}.json'.format(
                self.mongoexports_dir, self.dbname, item['source_coll'])
            template_data['infile'] = infile

            template_data['wrangled_outfile'] = item['wrangled_outfile']

            template_data['target_db'] = item['target_db']
            template_data['target_coll'] = item['target_coll']

            template_data['redirect'] = redirect
            self.render_template(template_name, template_data, outfile)

    def gen_migrate_db_omniscript(self):
        template_name = 'migrate_db_omniscript.txt'
        template_data = dict()
        template_data['dbname'] = self.dbname
        template_data['gen_timestamp'] = self.timestamp()
        outfile = '{}/migrate_db_{}_omniscript.sh'.format(
            self.shell_artifacts_dir, self.dbname)
        self.render_template(template_name, template_data, outfile)

    def target_databases_list(self):
        target_databases = dict()
        for c in self.collections:
            source = self.mapping_data['source_dbname']
            target = c['mapping']['target_dbname']
            target_databases[target] = source
        return sorted(target_databases.keys())

    def gen_adf_linked_services(self):
        outdir = self.config.adf_linked_svc_artifacts_dir()
        template_data = dict()

        # One Storage Blob Linked Service
        template_name = 'adf_blob_linked_service.txt'
        name = self.config.blob_linked_service_name()
        outfile = '{}/{}.json'.format(outdir, name)
        template_data = dict()
        template_data['name'] = name
        self.render_template(template_name, template_data, outfile)

        # One CosmosMongo Linked Service per target database
        for target_db in self.target_databases_list():
            template_name = 'adf_cosmos_mongo_linked_service.txt'
            name = self.config.cosmos_linked_service_name(target_db)
            outfile = '{}/{}.json'.format(outdir, name)
            template_data = dict()
            template_data['name'] = name
            template_data['dbname'] = target_db
            self.render_template(template_name, template_data, outfile)

    def gen_adf_blob_datasets(self):
        manifest = self.get_manifest()
        datasets = manifest.adf_blob_datasets()
        outdir   = self.config.adf_dataset_artifacts_dir()
        template_data = dict()

        for dataset_name in sorted(datasets.keys()):
            outfile = '{}/{}.json'.format(outdir, dataset_name)
            template_name = 'adf_blob_directory_dataset.txt'
            template_data = dict()
            template_data['dataset_name']   = dataset_name
            template_data['blob_container'] = datasets[dataset_name]
            self.render_template(template_name, template_data, outfile)

    def gen_adf_cosmos_mongo_datasets(self):
        manifest = self.get_manifest()
        datasets = manifest.cosmos_target_datasets()
        outdir   = self.config.adf_dataset_artifacts_dir()

        for dataset_name in sorted(datasets.keys()):
            outfile = '{}/{}.json'.format(outdir, dataset_name)
            template_name = 'adf_cosmos_mongo_dataset.txt'
            template_data = datasets[dataset_name]
            self.render_template(template_name, template_data, outfile)

    def gen_adf_pipelines(self):
        manifest  = self.get_manifest()
        pipelines = manifest.get_merged_pipelines()
        outdir    = self.config.adf_pipeline_artifacts_dir()
        template_name = 'adf_copy_pipeline.txt'

        for pidx, pipeline in enumerate(pipelines):
            pipeline_name = pipeline['name']
            activities    = pipeline['activities']
            outfile = '{}/{}.json'.format(outdir, pipeline_name)
            template_data = dict()
            template_data['gen_timestamp'] = self.timestamp()
            template_data['pipeline_name'] = pipeline_name
            template_data['activities'] = activities
            self.render_template(template_name, template_data, outfile)

    def gen_adf_az_pipeline_scripts(self):
        manifest  = self.get_manifest()
        pipelines = manifest.get_merged_pipelines()
        outdir    = self.config.adf_pipeline_artifacts_dir()
        for p in pipelines:
            pname = p['name']
            template_name = 'adf_az_cli.txt'
            template_data = dict()
            template_data['gen_timestamp'] = self.timestamp()
            template_data['gen_by'] = 'artifact_generator.py gen_adf_az_pipeline_scripts()'
            template_data['p'] = p
            outfile = '{}/adf_{}.sh'.format(
                self.shell_artifacts_dir, pname)
            self.render_template(template_name, template_data, outfile)

    def gen_target_cosmos_az_create(self):
        manifest = self.get_manifest()
        target_db = manifest.target_db_for_source_db(self.dbname)
        collection_names = manifest.collection_names_for_target_db(target_db)
        target_collection_objects = list()
        template_name = 'cosmos_db_containers_az_cli.txt'
        outfile = '{}/{}_cosmos_db_containers_az_cli.sh'.format(
            self.shell_artifacts_dir, target_db)

        template_data = dict()
        template_data['gen_timestamp'] = self.timestamp()
        template_data['gen_by'] = 'artifact_generator.py gen_target_cosmos_az_create()'
        template_data['authored_year_month'] = self.config.authored_year_month()
        template_data['target_db'] = target_db
        template_data['ru'] = self.mapping_data['cosmos_db_autoscale_ru']
        template_data['collections'] = target_collection_objects

        for target_coll in collection_names:
            info = dict()
            info['name'] = target_coll
            info['pk'] = manifest.pk_for_container(target_db, target_coll)
            target_collection_objects.append(info)

        self.render_template(template_name, template_data, outfile)

    def gen_target_cosmos_mongo_indexes(self):
        manifest = self.get_manifest()
        database_names = manifest.target_database_names()
        tuples = manifest.cosmos_target_db_coll_tuples()

        for dbname in database_names:
            template_data = dict()
            template_data['gen_timestamp'] = self.timestamp()
            template_data['gen_by'] = 'artifact_generator.py gen_target_cosmos_mongo_indexes()'
            template_data['authored_year_month'] = self.config.authored_year_month()
            template_data['dbname'] = dbname
            template_data['collections'] = list()
            for t in tuples:
                if (t[0] == dbname):
                    template_data['collections'].append(t[1])

            template_name = 'mongo_database_indexes.ddl'
            outdir = self.mongo_artifacts_dir
            outfile = '{}/mongo_indexes_{}_db.ddl'.format(outdir, dbname)
            self.render_template(template_name, template_data, outfile)

            template_name = 'mongo_database_indexes.txt'
            outdir = self.shell_artifacts_dir
            outfile = '{}/mongo_indexes_{}_db.sh'.format(outdir, dbname)
            self.render_template(template_name, template_data, outfile)

    def generate_reference_db_scripts(self):
        self.generate_openflights_reference_db_scripts()
        self.generate_olympics_reference_db_scripts()

    def generate_openflights_reference_db_scripts(self):
        dbname = 'openflights'
        outfile = '{}/databases/mongo_recreate_{}_db.sh'.format(
            self.config.app_dir, dbname)
        template_name = 'mongo_recreate_db.txt'
        template_data = dict()
        template_data['authored_year_month'] = self.config.authored_year_month()
        template_data['dbname'] = dbname
        template_data['gen_timestamp'] = self.timestamp()
        template_data['gen_by'] = 'artifact_generator.py generate_openflights_reference_db_scripts()'
        template_data['uri']  = self.config.source_mongodb_uri()
        template_data['url']  = self.config.source_mongodb_url
        template_data['host'] = self.config.source_mongodb_host 
        template_data['post'] = self.config.source_mongodb_port
        template_data['user'] = self.config.source_mongodb_user 
        template_data['pass'] = self.config.source_mongodb_pass
        template_data['ssl']  = ' # no --ssl' # self.config.source_mongodb_ssl 
        coll_names = self.openflights_collection_names()
        coll_list = list()
        for coll_name in coll_names:
            coll_info = dict()
            coll_info['name'] = coll_name
            coll_info['infile'] = '{}.json'.format(coll_name)
            coll_list.append(coll_info)
        template_data['collections'] = sorted(coll_list, key = itemgetter('name'))
        self.render_template(template_name, template_data, outfile)

    def openflights_collection_names(self):
        return 'airports,airlines,routes,planes,countries'.split(',')

    def generate_olympics_reference_db_scripts(self):
        dbname = 'olympics'
        template_name = 'mongo_recreate_db.txt'
        outfile = '{}/databases/mongo_recreate_{}_db.sh'.format(
            self.config.app_dir, dbname)
        template_data = dict()
        template_data['authored_year_month'] = self.config.authored_year_month()
        template_data['dbname'] = dbname
        template_data['gen_timestamp'] = self.timestamp()
        template_data['gen_by'] = 'artifact_generator.py generate_olympics_reference_db_scripts()'
        template_data['uri']  = self.config.source_mongodb_uri()
        template_data['url']  = self.config.source_mongodb_url
        template_data['host'] = self.config.source_mongodb_host 
        template_data['post'] = self.config.source_mongodb_port
        template_data['user'] = self.config.source_mongodb_user 
        template_data['pass'] = self.config.source_mongodb_pass
        template_data['ssl']  = ' # no --ssl' # self.config.source_mongodb_ssl 
        coll_names = self.olympics_collection_names()
        coll_list = list()
        for coll_name in coll_names:
            coll_info = dict()
            coll_info['name'] = coll_name
            coll_info['infile'] = '{}.json'.format(coll_name)
            coll_list.append(coll_info)
        template_data['collections'] = sorted(coll_list, key = itemgetter('name'))

        self.render_template(template_name, template_data, outfile)

    def olympics_collection_names(self):
        return [
            "countries",
            "g1896_summer",
            "g1900_summer",
            "g1904_summer",
            "g1906_summer",
            "g1908_summer",
            "g1912_summer",
            "g1920_summer",
            "g1924_summer",
            "g1924_winter",
            "g1928_summer",
            "g1928_winter",
            "g1932_summer",
            "g1932_winter",
            "g1936_summer",
            "g1936_winter",
            "g1948_summer",
            "g1948_winter",
            "g1952_summer",
            "g1952_winter",
            "g1956_summer",
            "g1956_winter",
            "g1960_summer",
            "g1960_winter",
            "g1964_summer",
            "g1964_winter",
            "g1968_summer",
            "g1968_winter",
            "g1972_summer",
            "g1972_winter",
            "g1976_summer",
            "g1976_winter",
            "g1980_summer",
            "g1980_winter",
            "g1984_summer",
            "g1984_winter",
            "g1988_summer",
            "g1988_winter",
            "g1992_summer",
            "g1992_winter",
            "g1994_winter",
            "g1996_summer",
            "g1998_winter",
            "g2000_summer",
            "g2002_winter",
            "g2004_summer",
            "g2006_winter",
            "g2008_summer",
            "g2010_winter",
            "g2012_summer",
            "g2014_winter",
            "g2016_summer",
            "games"
        ]

    def shell_script_lines(self):
        lines = list()
        if self.shell_type == 'bash':
            lines.append('#!/bin/bash')
            lines.append('')
            lines.append('# generated on: {}'.format(self.timestamp()))
            lines.append('')
        else:
            lines.append('')
            lines.append('# generated on: {}'.format(self.timestamp()))
            lines.append('')

    def timestamp(self):
        return arrow.utcnow().format('YYYY-MM-DD HH:mm:ss UTC')

    def env_var(self, name, default_value=''):
        try:
            return os.environ[name]
        except:
            return default_value

    def _source_collection_names(self):
        names = list()
        for coll in self.collections:
            names.append(coll['name'])
        return names

    def load_json_file(self, infile):
        with open(infile) as json_file:
            return json.load(json_file)

    def ensure_directory_path(self, dir_path):
        try:
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
        except:
            pass

    def render_template(self, template_name, template_data, outfile):
        t = self.get_template(os.getcwd(), template_name)
        s = t.render(template_data)
        self.write(outfile, s)

    def get_template(self, root_dir, name):
        filename = 'templates/{}'.format(name)
        return self.get_jinja2_env(root_dir).get_template(filename)

    def get_jinja2_env(self, root_dir):
        return jinja2.Environment(
            loader = jinja2.FileSystemLoader(
                root_dir), autoescape=True)

    def write(self, outfile, s, verbose=True):
        with open(outfile, 'w') as f:
            f.write(s)
            if verbose:
                print('file written: {}'.format(outfile))

    def write_obj_as_json_file(self, outfile, obj):
        txt = json.dumps(obj, sort_keys=False, indent=2)
        with open(outfile, 'wt') as f:
            f.write(txt)
        print("file written: " + outfile)

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

    def read_lines(self, infile):
        lines = list()
        with open(infile, 'rt') as f:
            for line in f:
                lines.append(line)
        return lines
