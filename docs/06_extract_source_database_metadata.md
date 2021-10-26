# 06 - Extract Source Database Metadata

In this section you excute script **extract_metadata.sh** which executes a 
python program, which uses the pymongo library, to read the metadata from 
the source MongoDB databases.

**This step is typically executed from a Developer laptop.**

## Execute script generate_initial_scripts.sh

In the **m2c/** directory, execute this script:

```
$ ./extract_metadata.sh
```

Which produces the following output (with the reference databases):

```
dbname:   olympics
conn_str: mongodb://root:rootpassword@localhost:27017/admin
client: MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
db: Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'olympics')
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/metadata/olympics_metadata.json
dbname:   openflights
conn_str: mongodb://root:rootpassword@localhost:27017/admin
client: MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)
db: Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'openflights')
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/metadata/openflights_metadata.json
done
```

The output files are written to the location within your $M2C_APP_DATA_DIR, in the **metadata** subdirectory.

## Sample Metadata

The metadata for the **openflights** database looks like the following.  Notice how
information about each collection is extracted.

```
{
  "dbname": "openflights",
  "utc_datetime": "2021-06-12T21:40:47.399520+00:00",
  "collections": [
    {
      "name": "countries",
      "metadata": {
        "doc_count": 261,
        "indexes": [
          {
            "v": 2,
            "key": {
              "_id": 1
            },
            "name": "_id_"
          }
        ],
        "stats": {
          "ns": "openflights.countries",
          "size": 20643,
          "count": 261,
          "avgObjSize": 79,
          "storageSize": 24576,
          "freeStorageSize": 0,
          "capped": false,
          "nindexes": 1,
          "indexBuilds": [],
          "totalIndexSize": 20480,
          "totalSize": 45056,
          "indexSizes": {
            "_id_": 20480
          },
          "scaleFactor": 1,
          "ok": 1.0
        }
      }
    },
    {
      "name": "airports",
      "metadata": {
        "doc_count": 7698,
        "indexes": [
          {
            "v": 2,
            "key": {
              "_id": 1
            },
            "name": "_id_"
          }
        ],
        "stats": {
          "ns": "openflights.airports",
          "size": 2626623,
          "count": 7698,
          "avgObjSize": 341,
          "storageSize": 909312,
          "freeStorageSize": 12288,
          "capped": false,
          "nindexes": 1,
          "indexBuilds": [],
          "totalIndexSize": 98304,
          "totalSize": 1007616,
          "indexSizes": {
            "_id_": 98304
          },
          "scaleFactor": 1,
          "ok": 1.0
        }
      }
    },
    {
      "name": "routes",
      "metadata": {
        "doc_count": 67663,
        "indexes": [
          {
            "v": 2,
            "key": {
              "_id": 1
            },
            "name": "_id_"
          }
        ],
        "stats": {
          "ns": "openflights.routes",
          "size": 15503770,
          "count": 67663,
          "avgObjSize": 229,
          "storageSize": 2412544,
          "freeStorageSize": 86016,
          "capped": false,
          "nindexes": 1,
          "indexBuilds": [],
          "totalIndexSize": 651264,
          "totalSize": 3063808,
          "indexSizes": {
            "_id_": 651264
          },
          "scaleFactor": 1,
          "ok": 1.0
        }
      }
    },
    {
      "name": "airlines",
      "metadata": {
        "doc_count": 6161,
        "indexes": [
          {
            "v": 2,
            "key": {
              "_id": 1
            },
            "name": "_id_"
          }
        ],
        "stats": {
          "ns": "openflights.airlines",
          "size": 1048944,
          "count": 6161,
          "avgObjSize": 170,
          "storageSize": 372736,
          "freeStorageSize": 0,
          "capped": false,
          "nindexes": 1,
          "indexBuilds": [],
          "totalIndexSize": 69632,
          "totalSize": 442368,
          "indexSizes": {
            "_id_": 69632
          },
          "scaleFactor": 1,
          "ok": 1.0
        }
      }
    },
    {
      "name": "planes",
      "metadata": {
        "doc_count": 246,
        "indexes": [
          {
            "v": 2,
            "key": {
              "_id": 1
            },
            "name": "_id_"
          }
        ],
        "stats": {
          "ns": "openflights.planes",
          "size": 19699,
          "count": 246,
          "avgObjSize": 80,
          "storageSize": 24576,
          "freeStorageSize": 0,
          "capped": false,
          "nindexes": 1,
          "indexBuilds": [],
          "totalIndexSize": 20480,
          "totalSize": 45056,
          "indexSizes": {
            "_id_": 20480
          },
          "scaleFactor": 1,
          "ok": 1.0
        }
      }
    }
  ],
  "dbstats": {
    "db": "openflights",
    "collections": 5,
    "views": 0,
    "objects": 82029,
    "avgObjSize": 234.3034658474442,
    "dataSize": 19219679.0,
    "storageSize": 3743744.0,
    "indexes": 5,
    "indexSize": 860160.0,
    "totalSize": 4603904.0,
    "scaleFactor": 1.0,
    "fsUsedSize": 18937679872.0,
    "fsTotalSize": 67371577344.0,
    "ok": 1.0
  }
}
```