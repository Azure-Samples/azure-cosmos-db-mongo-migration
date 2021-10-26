__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "July 2021"

import arrow
import os
import time
import pytest

from pysrc.config import Config

# This file implements unit tests of class Config, using the pytest framework.

def test_instance_variables():
    config = Config()
    assert(config.shell_type == 'bash')
    assert(config.ssl == False)
    assert(config.artifacts_dir.endswith('reference_app/artifacts'))
    assert(config.data_dir.endswith('reference_app/data'))
    assert(config.app_dir.endswith('reference_app'))
    assert(config.source_mongodb_url  == 'localhost:27017')
    assert(config.source_mongodb_host == 'localhost')
    assert(config.source_mongodb_port == '27017')
    assert(config.source_mongodb_user == 'root')
    assert(config.source_mongodb_pass == 'rootpassword')
    assert(config.source_mongodb_ssl  == False)

def test_migrated_databases_list_file():
    config = Config()
    expected = 'reference_app/data/metadata/migrated_databases_list.txt'
    assert(config.migrated_databases_list_file().endswith(expected))

def test_source_mongodb_uri():
    config = Config()
    assert(config.source_mongodb_uri() == 'mongodb://@localhost:27017')

def test_source_pymongo_conn_string():
    config = Config()
    expected = 'mongodb://root:rootpassword@localhost:27017/admin'
    assert(config.source_pymongo_conn_string('admin') == expected)

def test_metadata_dir():
    config = Config()
    expected = 'reference_app/data/metadata'
    assert(config.metadata_dir().endswith(expected))

def test_metadata_file():
    config = Config()
    expected = 'reference_app/data/metadata/olympics_metadata.json'
    f = config.db_metadata_file('olympics')
    assert(f.endswith(expected))

def test_metadata_files():
    config = Config()
    expected1 = 'reference_app/data/metadata/olympics_metadata.json'
    expected2 = 'reference_app/data/metadata/openflights_metadata.json'
    files = sorted(config.metadata_files())
    assert(files[0].endswith(expected1))
    assert(files[1].endswith(expected2))

def test_manifest_csv_file():
    config = Config()
    assert(config.manifest_csv_file().endswith('reference_app/data/metadata/manifest.csv'))

def test_manifest_json_file():
    config = Config()
    assert(config.manifest_json_file().endswith('reference_app/data/metadata/manifest.json'))

def test_mapping_file():
    config = Config()
    expected =  'reference_app/data/metadata/olympics_mapping.json'
    f = config.db_mapping_file('olympics')
    assert(f.endswith(expected))

def test_mongoexports_dir():
    config = Config()
    expected = 'reference_app/data/mongoexports/olympics'
    f = config.mongoexports_dir('olympics')
    assert(f.endswith(expected))

def test_mongoexports_file():
    config = Config()
    expected = 'reference_app/data/mongoexports/olympics/olympics__countries.json'
    f = config.mongoexport_file('olympics', 'countries')
    assert(f.endswith(expected))

def test_blob_raw_container_name():
    config = Config()
    expected = 'olympics-raw'
    f = config.blob_raw_container_name('olympics')
    assert(f.endswith(expected))

def test_blob_adf_container_name():
    config = Config()
    expected = 'db-coll-adf'
    f = config.blob_adf_container_name('db', 'coll')
    assert(f.endswith(expected))

def test_blob_download_dir():
    config = Config()
    expected = 'reference_app/data/downloads/olympics'
    f = config.blob_download_dir('olympics')
    assert(f.endswith(expected))

def test_wrangling_blob_download_file():
    config = Config()
    expected = 'tmp/olympics/olympics__countries.json'
    f = config.wrangling_blob_download_file('olympics', 'countries')
    assert(f.endswith(expected))

def test_wrangle_script_basename():
    config = Config()
    expected = 'olympics/wrangle_olympics_countries'
    s = config.wrangle_script_basename('olympics', 'countries')
    assert(s.endswith(expected))

def test_wrangle_script_name():
    config = Config()
    expected = 'wrangle_olympics_countries.sh'
    s = config.wrangle_script_name('olympics', 'countries')
    assert(s.endswith(expected))

def test_wrangled_file_name():
    config = Config()
    expected = 'olympics__countries__wrangled.json'
    s = config.wrangled_file_name('olympics', 'countries')
    print(s)
    assert(s == expected)

def test_wrangled_outfile():
    config = Config()
    expected = 'tmp/olympics/olympics__countries__wrangled.json'
    s = config.wrangled_outfile('olympics', 'countries')
    assert(s.endswith(expected))

def test_shell_artifacts_dir():
    config = Config()
    expected = 'reference_app/artifacts/shell'
    f = config.shell_artifacts_dir()
    assert(f.endswith(expected))

def test_adf_artifacts_dir():
    config = Config()
    expected = 'reference_app/artifacts/adf'
    f = config.adf_artifacts_dir()
    assert(f.endswith(expected))

def test_adf_linked_svc_artifacts_dir():
    config = Config()
    expected = 'reference_app/artifacts/adf/linkedService'
    f = config.adf_linked_svc_artifacts_dir()
    assert(f.endswith(expected))

def test_adf_dataset_artifacts_dir():
    config = Config()
    expected = 'reference_app/artifacts/adf/dataset'
    f = config.adf_dataset_artifacts_dir()
    assert(f.endswith(expected))

def test_adf_pipeline_artifacts_dir():
    config = Config()
    expected = 'reference_app/artifacts/adf/pipeline'
    s = config.adf_pipeline_artifacts_dir()
    assert(s.endswith(expected))

def test_adf_pipeline_name():
    config = Config()
    expected = 'pipeline_copy_to_openflights_routes'
    s = config.adf_pipeline_name('openflights', 'routes')
    assert(s.endswith(expected))

def test_blob_linked_service_name():
    config = Config()
    assert(config.blob_linked_service_name() == 'M2CMigrationBlobStorage')

def test_blob_dataset_name():
    config = Config()
    expected = 'blob__openflights__routes'
    s = config.blob_dataset_name('openflights', 'routes')
    assert(s.endswith(expected))

def test_cosmos_linked_service_name():
    config = Config()
    expected = 'M2CMigrationCosmosDB_openflights'
    s = config.cosmos_linked_service_name('openflights')
    assert(s == expected)

def test_cosmos_dataset_name():
    config = Config()
    expected = 'cosmos__openflights__routes'
    s = config.cosmos_dataset_name('openflights', 'routes')
    assert(s.endswith(expected))

def test_reference_app_databases_dir():
    config = Config()
    assert(config.reference_app_databases_dir().endswith('reference_app/databases'))

def test_mongo_artifacts_dir():
    config = Config()
    expected = 'reference_app/artifacts/shell/mongo'
    s = config.mongo_artifacts_dir()
    assert(s.endswith(expected))

# def test_ensure_directory_path():
#     config = Config()
#     dirname = 'tmp/{}'.format(int(time.time()))
#     result = config.ensure_directory_path(dirname)
#     assert(result == 'created')
#     result = config.ensure_directory_path(dirname)
#     assert(result == 'exists')
#     result = config.ensure_directory_path(None)
#     assert(result == 'except')

def test_timestamp():
    config = Config()
    ts = config.timestamp()  # '2021-05-29 10:44:39 UTC'
    assert(ts.startswith('2021-')) 
    assert(ts.endswith(' UTC'))
    assert(len(ts) == 23)
    assert(len(ts.split()) == 3)

def test_env_var():
    config = Config()
    assert(len(config.env_var('HOME', '')) > 0)
    assert(config.env_var('ARE_YOU_THERE', 'no') == 'no')

def test_boolean_env_var():
    config = Config()
    assert(config.boolean_env_var('HOME', False) == False)
    assert(config.boolean_env_var('HOME', True) == False)
    assert(config.boolean_env_var('ABSENT', False) == False)
    assert(config.boolean_env_var('ABSENT', True) == True)

    os.environ['AUTOMATED'] = 'TRUE'
    os.environ['MANUAL'] = 'FALSE'
    assert(config.boolean_env_var('AUTOMATED', False) == True)
    assert(config.boolean_env_var('MANUAL', True) == False)

def test_authored_year_month():
    config = Config()
    assert(config.authored_year_month() == 'July 2021')
