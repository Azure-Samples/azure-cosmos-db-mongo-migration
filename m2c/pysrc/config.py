__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "October 2021"

import arrow
import glob
import os
import sys
import traceback
import uuid

# Class Config is used by the application to:
# 1) obtain all configuration values, such as environment variables.  
# 2) defines all directory and file names
# 3) define/create other computed string values, such as for code generation

class Config(object):

    def __init__(self):
        self.shell_type          = self.env_var('M2C_SHELL_TYPE', 'bash')
        self.ssl                 = self.boolean_env_var('M2C_SOURCE_MONGODB_SSL', True)
        self.app_dir             = self.env_var('M2C_APP_DIR', None)
        self.artifact_types      = self.env_var('M2C_APP_ARTIFACTS', '--all') 
        self.artifacts_dir       = self.env_var('M2C_APP_ARTIFACTS_DIR', 'artifacts')
        self.data_dir            = self.env_var('M2C_APP_DATA_DIR', 'data') 
        self.source_mongodb_url  = self.env_var('M2C_SOURCE_MONGODB_URL', 'localhost:27017')
        self.source_mongodb_host = self.env_var('M2C_SOURCE_MONGODB_HOST', 'localhost')
        self.source_mongodb_port = self.env_var('M2C_SOURCE_MONGODB_PORT', '27017')
        self.source_mongodb_user = self.env_var('M2C_SOURCE_MONGODB_USER', 'root')
        self.source_mongodb_pass = self.env_var('M2C_SOURCE_MONGODB_PASS', 'rootpassword')
        self.source_mongodb_ssl  = self.boolean_env_var('M2C_SOURCE_MONGODB_SSL',  False)

    def source_mongodb_uri(self):
        return 'mongodb://@{}:{}'.format(
            self.source_mongodb_host, self.source_mongodb_port)

    def source_pymongo_conn_string(self, dbname):
        # https://docs.mongodb.com/manual/reference/connection-string/
        # mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]
        return 'mongodb://{}:{}@{}:{}/{}'.format(
            self.source_mongodb_user,
            self.source_mongodb_pass,
            self.source_mongodb_host,
            self.source_mongodb_port,
            dbname)

    def metadata_dir(self):
        return '{}/metadata'.format(self.data_dir)

    def metadata_files(self):
        pattern = '{}/*_metadata.json'.format(self.metadata_dir())
        return glob.glob(pattern)

    def migrated_databases_list_file(self):
        return '{}/migrated_databases_list.txt'.format(self.metadata_dir())

    def db_metadata_file(self, dbname):
        outdir = self.metadata_dir()
        return '{}/{}_metadata.json'.format(outdir, dbname)

    def manifest_csv_file(self):
        return '{}/manifest.csv'.format(self.metadata_dir())

    def manifest_json_file(self):
        return '{}/manifest.json'.format(self.metadata_dir())

    def db_mapping_file(self, dbname):
        outdir = self.metadata_dir()
        return '{}/{}_mapping.json'.format(outdir, dbname)

    def mongoexports_dir(self, dbname):
        return '{}/mongoexports/{}'.format(self.data_dir, dbname)

    def mongoexport_file(self, dbname, cname):
        return '{}/{}__{}.json'.format(
            self.mongoexports_dir(dbname), dbname, cname)

    def shell_artifacts_dir(self):
        return '{}/shell'.format(self.artifacts_dir)

    def mongo_artifacts_dir(self):
        return '{}/shell/mongo'.format(self.artifacts_dir)

    def adf_artifacts_dir(self):
        return '{}/adf'.format(self.artifacts_dir)

    def adf_linked_svc_artifacts_dir(self):
        return '{}/adf/linkedService'.format(self.artifacts_dir)

    def adf_dataset_artifacts_dir(self):
        return '{}/adf/dataset'.format(self.artifacts_dir)

    def adf_pipeline_artifacts_dir(self):
        return '{}/adf/pipeline'.format(self.artifacts_dir)

    def adf_pipeline_name(self, target_db, target_coll):
        return 'pipeline_copy_to_{}_{}'.format(target_db, target_coll)

    def blob_name(self, source_db, source_coll):
        return '{}__{}.json'.format(source_db, source_coll)

    def wrangled_file_name(self, dbname, cname):
        return '{}__{}__wrangled.json'.format(dbname, cname)

    def blob_raw_container_name(self, source_db):
        return '{}-raw'.format(source_db)

    def blob_adf_container_name(self, target_db, target_coll):
        return '{}-{}-adf'.format(target_db, target_coll)

    def blob_download_dir(self, dbname):
        return '{}/downloads/{}'.format(self.data_dir, dbname)

    def wrangling_blob_download_file(self, dbname, cname):
        return 'tmp/{}/{}'.format(
            dbname, self.blob_name(dbname, cname))

    def wrangled_outfile(self, dbname, cname):
        return 'tmp/{}/{}'.format(
            dbname, self.wrangled_file_name(dbname, cname))

    def wrangle_script_basename(self, dbname, cname):
        return '{}/wrangle_{}_{}'.format(dbname, dbname, cname)

    def wrangle_script_name(self, dbname, cname):
        return 'wrangle_{}_{}.sh'.format(dbname, cname)

    def blob_linked_service_name(self):
        return 'M2CMigrationBlobStorage'

    def blob_dataset_name(self, target_db, target_coll):
        return 'blob__{}__{}'.format(target_db, target_coll)

    def cosmos_linked_service_name(self, target_db):
        return 'M2CMigrationCosmosDB_{}'.format(target_db)

    def cosmos_dataset_name(self, dbname, cname):
        return 'cosmos__{}__{}'.format(dbname, cname)

    def reference_app_databases_dir(self):
        return '{}/databases'.format(self.app_dir) 

    def timestamp(self):
        return arrow.utcnow().format('YYYY-MM-DD HH:mm:ss UTC')

    def authored_year_month(self):
        return 'October 2021'

    def env_var(self, name, default_value=''):
        try:
            return os.environ[name]
        except:
            return default_value

    def boolean_env_var(self, name, default_value):
        try:
            v = os.environ[name].lower()
            if (v.lower() == 'true') or (v.lower() == 't'):
                return True
            return False
        except:
            return default_value
