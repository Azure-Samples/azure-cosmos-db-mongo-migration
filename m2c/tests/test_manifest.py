__author__  = 'Chris Joakim'
__email__   = "chjoakim@microsoft.com"
__license__ = "MIT"
__version__ = "July 2021"

import arrow
import json
import os
import time
import pytest

from pysrc.manifest import Manifest

# This file implements unit tests of class Manifest, using the pytest framework.

def test_constructor():
    m = Manifest()
    assert(len(m.items) == 58)     # source collection count
    assert(len(m.pipelines) == 7)  # target collection count

def test_source_database_names():
    m = Manifest()
    assert(m.source_database_names() == ['olympics', 'openflights'])

def test_target_database_names():
    m = Manifest()
    assert(m.target_database_names() == ['olympics', 'travel'])

def test_storage_container_names():
    m = Manifest()
    names = m.storage_container_names()
    write_obj_as_json_file('tmp/storage_container_names.json', names)
    expected = expected_storage_container_names()
    assert(names == expected)

def test_adf_blob_datasets():
    m = Manifest()
    names = m.adf_blob_datasets()
    write_obj_as_json_file('tmp/adf_blob_datasets.json', names)
    hash = expected_adf_blob_datasets()
    assert(len(hash.keys()) == 7)
    assert(hash['blob__travel__airlines'] == 'travel-airlines-adf')

def test_cosmos_target_datasets():
    m = Manifest()
    datasets = m.cosmos_target_datasets()
    write_obj_as_json_file('tmp/cosmos_target_datasets.json', datasets)
    expected = expected_cosmos_target_datasets()
    assert(len(datasets.keys()) == 7)
    for key in datasets.keys():
        assert(datasets[key] == expected[key])

def test_items_for_source_db():
    m = Manifest()
    assert(len(m.items_for_source_db('nope')) == 0)
    assert(len(m.items_for_source_db('olympics')) == 53)
    assert(len(m.items_for_source_db('openflights')) == 5)

    items = m.items_for_source_db('openflights')
    write_obj_as_json_file('tmp/items_for_source_db.json', items)

    expected = {
      "source_db": "openflights",
      "source_coll": "routes",
      "doc_count": "67663",
      "avg_doc_size": "229",
      "target_db": "travel",
      "target_coll": "routes",
      "partition_key": "pk",
      "blob_name": "openflights__routes.json",
      "raw_storage_container": "openflights-raw",
      "adf_storage_container": "travel-routes-adf",
      "adf_blob_doc_count": "-1",
      "adf_blob_dataset_name": "blob__travel__routes",
      "adf_cosmos_dataset_name": "cosmos__travel__routes",
      "adf_pipeline_name": "pipeline_copy_to_travel_routes",
      "mongoexports_dir": "/Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights",
      "mongoexport_file": "/Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__routes.json",
      "wrangle_script_name": "wrangle_openflights_routes.sh",
      "wrangled_outfile": "tmp/openflights/openflights__routes__wrangled.json",
      "wrangled_blob_name": "openflights__routes__wrangled.json",
      "local_file_path": "tmp/openflights/openflights__routes.json"
    }
    assert(items[-1] == expected)

def test_wrangle_script_names_for_source_db():
    m = Manifest()
    names = m.wrangle_script_names_for_source_db('olympics')
    write_obj_as_json_file('tmp/wrangle_script_names_for_source_db.json', names)
    assert(names == expected_wrangle_script_names_for_olympics_db())

def test_cosmos_source_db_coll_tuples():
    m = Manifest()
    tuples = m.cosmos_source_db_coll_tuples()
    write_obj_as_json_file('tmp/cosmos_source_db_coll_tuples.json', tuples)
    assert(len(tuples) == 58)
    assert(tuples[-1] == ('openflights', 'routes'))

def test_cosmos_target_db_coll_tuples():
    m = Manifest()
    tuples = m.cosmos_target_db_coll_tuples()
    write_obj_as_json_file('tmp/cosmos_target_db_coll_tuples.json', tuples)
    assert(len(tuples) == 7)
    assert(tuples[-1] == ('travel', 'routes'))

def test_cosmos_mapping_tuples():
    m = Manifest()
    tuples = m.cosmos_mapping_tuples()
    write_obj_as_json_file('tmp/cosmos_mapping_tuples.json', tuples)
    assert(len(tuples) == 58)
    assert(tuples[-1] == ('openflights', 'routes', 'travel', 'routes'))

def test_target_db_for_source_db():
    m = Manifest()
    assert('olympics' == m.target_db_for_source_db('olympics'))
    assert('travel' == m.target_db_for_source_db('openflights'))
    assert(None == m.target_db_for_source_db('oops'))

def test_collection_names_for_target_db():
    m = Manifest()
    names = m.collection_names_for_target_db('olympics')
    assert(names == ['games', 'locations'])
    names = m.collection_names_for_target_db('travel')
    assert(names == ['airlines', 'airports', 'countries', 'planes', 'routes'])
    names = m.collection_names_for_target_db('oops')
    assert(names == [])

def test_pk_for_container():
    m = Manifest()
    assert('pk' == m.pk_for_container('olympics', 'locations'))
    assert('pk' == m.pk_for_container('travel', 'routes'))
    assert(None == m.pk_for_container('not', 'there'))

def test_get_merged_pipelines():
    m = Manifest()
    p = m.get_merged_pipelines()
    m.write_obj_as_json_file('tmp/get_merged_pipelines.json', p)
    assert(len(p) == 7)

    expected = {
        "name": "pipeline_copy_to_olympics_games",
        "activities": [
            {
                "name": "copy_blob__olympics__games",
                "input_dataset": "blob__olympics__games",
                "output_dataset": "cosmos__olympics__games",
                "has_dependency": False,
                "dependent_activity": "",
                "activity_sep": ""
            }
        ]
    }
    assert(p[0] == expected)

def test_read_migrated_databases_list_file():
    m = Manifest()
    dbs = m.read_migrated_databases_list_file()
    assert(dbs == ['olympics', 'openflights'])


def expected_storage_container_names():
    return [
        "olympics-games-adf",
        "olympics-locations-adf",
        "olympics-raw",
        "openflights-raw",
        "travel-airlines-adf",
        "travel-airports-adf",
        "travel-countries-adf",
        "travel-planes-adf",
        "travel-routes-adf"
    ]

def expected_adf_blob_datasets():
    return {
        "blob__olympics__locations": "olympics-locations-adf",
        "blob__olympics__games": "olympics-games-adf",
        "blob__travel__airlines": "travel-airlines-adf",
        "blob__travel__airports": "travel-airports-adf",
        "blob__travel__countries": "travel-countries-adf",
        "blob__travel__planes": "travel-planes-adf",
        "blob__travel__routes": "travel-routes-adf"
    }

def expected_cosmos_target_datasets():
    return {
        "cosmos__olympics__locations": {
            "dataset_name": "cosmos__olympics__locations",
            "target_db": "olympics",
            "target_coll": "locations",
            "linked_svc": "M2CMigrationCosmosDB_olympics"
        },
        "cosmos__olympics__games": {
            "dataset_name": "cosmos__olympics__games",
            "target_db": "olympics",
            "target_coll": "games",
            "linked_svc": "M2CMigrationCosmosDB_olympics"
        },
        "cosmos__travel__airlines": {
            "dataset_name": "cosmos__travel__airlines",
            "target_db": "travel",
            "target_coll": "airlines",
            "linked_svc": "M2CMigrationCosmosDB_travel"
        },
        "cosmos__travel__airports": {
            "dataset_name": "cosmos__travel__airports",
            "target_db": "travel",
            "target_coll": "airports",
            "linked_svc": "M2CMigrationCosmosDB_travel"
        },
        "cosmos__travel__countries": {
            "dataset_name": "cosmos__travel__countries",
            "target_db": "travel",
            "target_coll": "countries",
            "linked_svc": "M2CMigrationCosmosDB_travel"
        },
        "cosmos__travel__planes": {
            "dataset_name": "cosmos__travel__planes",
            "target_db": "travel",
            "target_coll": "planes",
            "linked_svc": "M2CMigrationCosmosDB_travel"
        },
        "cosmos__travel__routes": {
            "dataset_name": "cosmos__travel__routes",
            "target_db": "travel",
            "target_coll": "routes",
            "linked_svc": "M2CMigrationCosmosDB_travel"
        }
    }

def expected_wrangle_script_names_for_olympics_db():
    return [
        "wrangle_olympics_countries.sh",
        "wrangle_olympics_g1896_summer.sh",
        "wrangle_olympics_g1900_summer.sh",
        "wrangle_olympics_g1904_summer.sh",
        "wrangle_olympics_g1906_summer.sh",
        "wrangle_olympics_g1908_summer.sh",
        "wrangle_olympics_g1912_summer.sh",
        "wrangle_olympics_g1920_summer.sh",
        "wrangle_olympics_g1924_summer.sh",
        "wrangle_olympics_g1924_winter.sh",
        "wrangle_olympics_g1928_summer.sh",
        "wrangle_olympics_g1928_winter.sh",
        "wrangle_olympics_g1932_summer.sh",
        "wrangle_olympics_g1932_winter.sh",
        "wrangle_olympics_g1936_summer.sh",
        "wrangle_olympics_g1936_winter.sh",
        "wrangle_olympics_g1948_summer.sh",
        "wrangle_olympics_g1948_winter.sh",
        "wrangle_olympics_g1952_summer.sh",
        "wrangle_olympics_g1952_winter.sh",
        "wrangle_olympics_g1956_summer.sh",
        "wrangle_olympics_g1956_winter.sh",
        "wrangle_olympics_g1960_summer.sh",
        "wrangle_olympics_g1960_winter.sh",
        "wrangle_olympics_g1964_summer.sh",
        "wrangle_olympics_g1964_winter.sh",
        "wrangle_olympics_g1968_summer.sh",
        "wrangle_olympics_g1968_winter.sh",
        "wrangle_olympics_g1972_summer.sh",
        "wrangle_olympics_g1972_winter.sh",
        "wrangle_olympics_g1976_summer.sh",
        "wrangle_olympics_g1976_winter.sh",
        "wrangle_olympics_g1980_summer.sh",
        "wrangle_olympics_g1980_winter.sh",
        "wrangle_olympics_g1984_summer.sh",
        "wrangle_olympics_g1984_winter.sh",
        "wrangle_olympics_g1988_summer.sh",
        "wrangle_olympics_g1988_winter.sh",
        "wrangle_olympics_g1992_summer.sh",
        "wrangle_olympics_g1992_winter.sh",
        "wrangle_olympics_g1994_winter.sh",
        "wrangle_olympics_g1996_summer.sh",
        "wrangle_olympics_g1998_winter.sh",
        "wrangle_olympics_g2000_summer.sh",
        "wrangle_olympics_g2002_winter.sh",
        "wrangle_olympics_g2004_summer.sh",
        "wrangle_olympics_g2006_winter.sh",
        "wrangle_olympics_g2008_summer.sh",
        "wrangle_olympics_g2010_winter.sh",
        "wrangle_olympics_g2012_summer.sh",
        "wrangle_olympics_g2014_winter.sh",
        "wrangle_olympics_g2016_summer.sh",
        "wrangle_olympics_games.sh"
    ]

def write_obj_as_json_file(outfile, obj):
    txt = json.dumps(obj, sort_keys=False, indent=2)
    with open(outfile, 'wt') as f:
        f.write(txt)
    print("file written: " + outfile)

