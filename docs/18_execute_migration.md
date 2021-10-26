# 18 - Execute Migration

The previous documentation pages 00 through 15 have explained the migration
process, setup various environments, and generated various artifacts.  In this page 
we finally **execute the migration process!**

The architecture diagram is repeated here:

<p align="center"><img src="img/architecture.png" width="99%"></p>

**These steps are typically executed from an Azure VM, though submitting the ADF pipelines can be done from a Developer laptop.**

---

## mongoexports

In the **artifacts/shell** directory there will be a generated file named
**xxx_mongoexports.sh**, where xxx is the name of one of your source databases.

The contents of these files will look like this:

```
#!/bin/bash

# Bash shell script to export each source collection via mongoexport.
#
# Database Name: openflights
# Generated on:  2021-06-13 13:18:15 UTC
# Template:      mongoexport_script.txt

source env.sh

mkdir -p data/source/mongoexports


echo ''
echo 'mongoexporting - database: openflights container: airlines'
mongoexport --authenticationDatabase admin -u $M2C_SOURCE_MONGODB_USER -p $M2C_SOURCE_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db openflights \
    --collection airlines \
    --out /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__airlines.json
     # no --ssl

echo ''
echo 'mongoexporting - database: openflights container: airports'
mongoexport --authenticationDatabase admin -u $M2C_SOURCE_MONGODB_USER -p $M2C_SOURCE_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db openflights \
    --collection airports \
    --out /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__airports.json
     # no --ssl

echo ''
echo 'mongoexporting - database: openflights container: countries'
mongoexport --authenticationDatabase admin -u $M2C_SOURCE_MONGODB_USER -p $M2C_SOURCE_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db openflights \
    --collection countries \
    --out /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__countries.json
     # no --ssl

echo ''
echo 'mongoexporting - database: openflights container: planes'
mongoexport --authenticationDatabase admin -u $M2C_SOURCE_MONGODB_USER -p $M2C_SOURCE_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db openflights \
    --collection planes \
    --out /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__planes.json
     # no --ssl

echo ''
echo 'mongoexporting - database: openflights container: routes'
mongoexport --authenticationDatabase admin -u $M2C_SOURCE_MONGODB_USER -p $M2C_SOURCE_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db openflights \
    --collection routes \
    --out /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__routes.json
     # no --ssl

echo 'done'
```

This script will execute the **mongoexport** program for each container in your source database.

It is **recommended** that the mongoexport process executes **close to the source database**,
such as an on-prem VM near your on-prem MongoDB, or a cloud VM near your cloud provider MongoDB.

The way the script is currently implemented the exports are executed sequentially on the same VM.
The project roadmap has a high-ranking item to **parallelize** the mongoexport process; this should
be a very easy enhancement to implement additional scripts for this.

Sample output:

```
$ ./openflights_mongoexports.sh

mongoexporting - database: openflights container: airlines
2021-06-14T11:32:31.520-0400	connected to: mongodb://[**REDACTED**]@localhost:27017
2021-06-14T11:32:31.932-0400	exported 18483 records

mongoexporting - database: openflights container: airports
2021-06-14T11:32:31.967-0400	connected to: mongodb://[**REDACTED**]@localhost:27017
2021-06-14T11:32:32.596-0400	exported 23094 records

mongoexporting - database: openflights container: countries
2021-06-14T11:32:32.633-0400	connected to: mongodb://[**REDACTED**]@localhost:27017
2021-06-14T11:32:32.658-0400	exported 783 records

mongoexporting - database: openflights container: planes
2021-06-14T11:32:32.691-0400	connected to: mongodb://[**REDACTED**]@localhost:27017
2021-06-14T11:32:32.713-0400	exported 738 records

mongoexporting - database: openflights container: routes
2021-06-14T11:32:32.745-0400	connected to: mongodb://[**REDACTED**]@localhost:27017
2021-06-14T11:32:33.749-0400	[####....................]  openflights.routes  40000/202989  (19.7%)
2021-06-14T11:32:34.746-0400	[###########.............]  openflights.routes  96000/202989  (47.3%)
2021-06-14T11:32:35.747-0400	[##################......]  openflights.routes  160000/202989  (78.8%)
2021-06-14T11:32:36.286-0400	[########################]  openflights.routes  202989/202989  (100.0%)
2021-06-14T11:32:36.286-0400	exported 202989 records
done
```

---

## Uploading the Raw mongoexport blobs to Azure Storage

This step is **intended to be executed from the same location/VM as the previous step, as the mongoexport files are local to that filesystem**.

Section [12 - Create the Azure Storage Containers](12_create_the_azure_storage_containers.md)
described the process to create the necessary storage containers in your Azure Storage account.
These containers are assumed to exist at this point.

Two equivalent sets of mongoexport file upload scripts are created; one uses
**python and Azure Storage SDK** while the other uses the **az CLI**.  Either can
be used depending on your preferences.

Execute one of these generated scripts per source database:

```
olympics_az_cli_mongoexport_uploads.sh
olympics_python_mongoexport_uploads.sh
openflights_az_cli_mongoexport_uploads.sh
openflights_python_mongoexport_uploads.sh
```

The way the script is currently implemented the uploads are executed sequentially on the same VM.
The project roadmap also has a high-ranking item to **parallelize** the uploads process; this should
also be a very easy enhancement to implement additional scripts for this.

### storage.py

There is a Python script, in the same directory, for accessing your Azure Storage Account.
The following functions are available:

```
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
```

---

## Data Wrangling of mongoimport files for CosmosDB

The purpose of the **Data Wrangling** process is to **transform the raw mongoexport**
files/blobs per your **mappings**.  The wrangling process runs on an **Azure VM**.

The generated wrangling scripts will download a raw blob to the VM, transform it,
then upload the transformed file to the Azure Storage container that corresponds
to the target CosmosDB target database and container.

### Three ways to load CosmosDB

This migration process implements three ways to load the transformed data into
CosmosDB.

- Azure Data Factory (ADF)
- mongoimport
- DotNet 5 custom loader program

You should edit file **env.sh**, as shown below, to use your preferred loading method.

```
export M2C_COSMOS_LOAD_METHOD="mongoimport"  # either adf or mongoimport or dotnet_mongo_loader
```

#### ADF Loading

The preferred method of populating CosmosDB with this transformed data is
**Azure Data Factory (ADF)**.  See section "Execute ADF Pipelines", below.
If this method is used, then the wrangling process will simply transform
the raw blob.

#### mongoimport and dotnet_mongo_loader Loading

Alternatively, there are two additional ways to load the transformed data into CosmosDB -
the **mongoimport** program from MongoDB, and a **DotNet 5 custom loader program**.

If either of these two methods is specified in **M2C_COSMOS_LOAD_METHOD** environment
variable, then the wrangling process will additionally directly load CosmosDB
with the transformed data.

See the m2c/dotnet_mongo_loader/ directory in this repo for the loader program.


### The generated scripts

The **artifacts/shell** directory will contain a number of generated **wrangle_**
scripts; one per source database, and one for each collection in each source database.

You can execute these all sequentially for a given source database, by executing the
**_all.sh** script.  Likewise, you can execute these scripts individually to parallelize
them.

For example, for the openflights reference database, the following are generated:

```
reference_app/artifacts/shell/wrangle_openflights_airlines.sh
reference_app/artifacts/shell/wrangle_openflights_airports.sh
reference_app/artifacts/shell/wrangle_openflights_countries.sh
reference_app/artifacts/shell/wrangle_openflights_planes.sh
reference_app/artifacts/shell/wrangle_openflights_routes.sh
reference_app/artifacts/shell/wrangle_openflights_all.sh   <-- executes each of the above
```


#### Example Wrangling Script

Each wrangling file looks like the following.

```
#!/bin/bash

# Bash shell script to wrangle/transform a raw mongoexport file.
#
# Database Name: olympics
# Generated on:  2021-07-30 21:52:55 UTC
# Template:      wrangle_one.txt

source ./env.sh

mkdir -p tmp/olympics/out
mkdir -p out/olympics

# This script does the following:
# 1) Downloads blob olympics__g1896_summer.json from container olympics-raw
#    to local file tmp/olympics/olympics__g1896_summer.json
# 2) Wrangle/transform the downloaded blob, producing local file 
#    tmp/olympics/olympics__g1896_summer__wrangled.json
# 3) Uploads the wrangled file to storage container olympics-adf
# 4) Optionally loads the target CosmosDB using the mongoimport program
# 5) Optionally loads the target CosmosDB using a custom DotNet program
# 6) Delete the downloaded and wrangled file, as the host VM may have limited storage
#
# Note: this script is executed by script olympics_wrangle_all.sh

python wrangle.py transform_blob \
    --db olympics \
    --source-coll  g1896_summer \
    --in-container olympics-raw \
    --blobname olympics__g1896_summer.json \
    --filename tmp/olympics/olympics__g1896_summer.json \
    --outfile  tmp/olympics/olympics__g1896_summer__wrangled.json \
    --out-container olympics-games-adf $1 $2 $3 

echo ''
echo 'first line of input file:'
head -1 tmp/olympics/olympics__g1896_summer.json

echo ''
echo 'first line of output file:'
head -1 tmp/olympics/olympics__g1896_summer__wrangled.json

if [[ $M2C_COSMOS_LOAD_METHOD == "mongoimport" ]];
then
    echo ''
    echo 'executing mongoimport to db: olympics coll: games ...' 

    mongoimport \
        --uri $M2C_COSMOS_MONGO_CONN_STRING \
        --db olympics \
        --collection games \
        --file tmp/olympics/olympics__g1896_summer__wrangled.json \
        --numInsertionWorkers $M2C_MONGOIMPORT_NWORKERS \
        --batchSize $M2C_MONGOIMPORT_BATCH_SIZE \
        --mode $M2C_MONGOIMPORT_MODE \
        --writeConcern "{w:0}" \
        --ssl

    echo 'mongoimport completed' 
fi 

if [[ $M2C_COSMOS_LOAD_METHOD == "dotnet_mongo_loader" ]];
then
    echo ''
    echo 'executing dotnet_mongo_loader to db: olympics coll: games ...' 

    dotnet run --project dotnet_mongo_loader/dotnet_mongo_loader.csproj \
        olympics games tmp/olympics/olympics__g1896_summer__wrangled.json \
        $M2C_DOTNETMONGOLOADER_TARGET $M2C_DOTNETMONGOLOADER_LOAD_IND \
        $M2C_DOTNETMONGOLOADER_DOCUMENT_ID_POLICY \
        --tracerInterval $M2C_DOTNETMONGOLOADER_TRACER_INTERVAL \
        --rowMaxRetries $M2C_DOTNETMONGOLOADER_ROW_MAX_RETRIES \
        $M2C_DOTNETMONGOLOADER_VERBOSE
fi

if [[ $M2C_WRANGLING_CLEANUP == "cleanup" ]];
then
    echo ''
    echo 'deleting the downloaded and wrangled files to save disk space...'
    rm tmp/olympics/olympics__g1896_summer.json
    rm tmp/olympics/olympics__g1896_summer__wrangled.json
fi

echo 'done'
```

It is important to note that the uploaded 
**wrangled blobs are written to the Azure Storage container that corresponds to a target CosmosDB database and collection**,
and not the source DB and container.  This design allows Azure Data Factory to read 
the one or more transofrmed files in each xxx-adf container as a single **dataset**.

Output from the above wrangling script:

```
$ ./wrangle_olympics_g1896_summer.sh
$ ./wrangle_olympics_g1896_summer.sh
__main__ args: ['wrangle.py', 'transform_blob', '--db', 'olympics', '--source-coll', 'g1896_summer', '--in-container', 'olympics-raw', '--blobname', 'olympics__g1896_summer.json', '--filename', 'tmp/olympics/olympics__g1896_summer.json', '--outfile', 'tmp/olympics/olympics__g1896_summer__wrangled.json', '--out-container', 'olympics-games-adf']
func: transform_blob
Transformer constructor; parsed args:
  dbname:        olympics
  source_coll:   g1896_summer
  in_container:  olympics-raw
  blobname:      olympics__g1896_summer.json
  filename:      tmp/olympics/olympics__g1896_summer.json
  outfile:       tmp/olympics/olympics__g1896_summer__wrangled.json
  out_container: olympics-games-adf
load_container_mappings; cname: g1896_summer
load_container_mappings; fname: olympics_mapping.json
mappings:
{
  "name": "g1896_summer",
  "mapping": {
    "target_dbname": "olympics",
    "target_container": "games",
    "wrangling_algorithm": "standard",
    "pk_name": "pk",
    "pk_logic": [
      [
        "attribute",
        "games"
      ]
    ],
    "pk_sep": "-",
    "doctype_name": "doctype",
    "doctype_logic": [
      [
        "dynamic",
        "source_cname"
      ]
    ],
    "doctype_sep": "-",
    "additions": [
      [
        "dynamic",
        "some_id",
        "uuid"
      ]
    ],
    "excludes": [
      "id"
    ]
  },
  "source_dbname": "olympics",
  "default_target_dbname": "olympics"
}
StandardDocumentWrangler constructor:
  do_pk_wrangling:      True
  do_doctype_wrangling: True
  do_additions:         True
  do_excludes:          True
wrangling_algorithm: standard
download_blob olympics__g1896_summer.json from olympics-raw to tmp/olympics/olympics__g1896_summer.json
download_blob: olympics-raw olympics__g1896_summer.json -> tmp/olympics/olympics__g1896_summer.json
downloaded tmp/olympics/olympics__g1896_summer.json in 0.4745049476623535ms
transformed 380 lines in 0.025618791580200195
uploading tmp/olympics/olympics__g1896_summer.json at 2021-06-15 17:46:28 UTC to olympics-games-adf/olympics__g1896_summer__wrangled.json
upload_blob: tmp/olympics/olympics__g1896_summer__wrangled.json True -> olympics-games-adf olympics__g1896_summer__wrangled.json
uploaded tmp/olympics/olympics__g1896_summer.json/olympics__g1896_summer__wrangled.json at 2021-06-15 17:46:28 UTC in 0.23813104629516602
{'name': 'olympics__g1896_summer__wrangled.json', 'container': 'olympics-games-adf', 'snapshot': None, 'version_id': None, 'is_current_version': None, 'blob_type': <BlobType.BlockBlob: 'BlockBlob'>, 'metadata': {}, 'encrypted_metadata': None, 'last_modified': datetime.datetime(2021, 6, 15, 17, 46, 29, tzinfo=datetime.timezone.utc), 'etag': '"0x8D9302581416DAE"', 'size': 155348, 'content_range': None, 'append_blob_committed_block_count': None, 'is_append_blob_sealed': None, 'page_blob_sequence_number': None, 'server_encrypted': True, 'copy': {'id': None, 'source': None, 'status': None, 'progress': None, 'completion_time': None, 'status_description': None, 'incremental_copy': None, 'destination_snapshot': None}, 'content_settings': {'content_type': 'application/octet-stream', 'content_encoding': None, 'content_language': None, 'content_md5': bytearray(b"\x93}\'\x13\xe6\x06\x1d\xac\xcc\xfc\r\xac;\x13l\xb3"), 'content_disposition': None, 'cache_control': None}, 'lease': {'status': 'unlocked', 'state': 'available', 'duration': None}, 'blob_tier': 'Hot', 'rehydrate_priority': None, 'blob_tier_change_time': None, 'blob_tier_inferred': True, 'deleted': False, 'deleted_time': None, 'remaining_retention_days': None, 'creation_time': datetime.datetime(2021, 6, 14, 19, 26, 41, tzinfo=datetime.timezone.utc), 'archive_status': None, 'encryption_key_sha256': None, 'encryption_scope': None, 'request_server_encrypted': True, 'object_replication_source_properties': [], 'object_replication_destination_policy': None, 'last_accessed_on': None, 'tag_count': None, 'tags': None}
-
SUMMARY for args:  wrangle.py transform_blob --db olympics --source-coll g1896_summer --in-container olympics-raw --blobname olympics__g1896_summer.json --filename tmp/olympics/olympics__g1896_summer.json --outfile tmp/olympics/olympics__g1896_summer__wrangled.json --out-container olympics-games-adf
  status:          completed
  lines_processed: 380
  start_time:      1623779188.210357
  elapsed_time:    0.7987241744995117

first line of input file:
{"_id":{"$oid":"60c7a7e05480299daf2e2090"},"id":"4113","name":"Anastasios Andreou","sex":"m","age":"-1","height":"-1","weight":"-1","team":"greece","noc":"gre","games":"1896_summer","year":"1896","season":"summer","city":"athina","sport":"athletics","event":"athletics mens 110 metres hurdles","medal":"","medal_value":"0"}

first line of output file:
{"_id":{"$oid":"60c7a7e05480299daf2e2090"},"name":"Anastasios Andreou","sex":"m","age":"-1","height":"-1","weight":"-1","team":"greece","noc":"gre","games":"1896_summer","year":"1896","season":"summer","city":"athina","sport":"athletics","event":"athletics mens 110 metres hurdles","medal":"","medal_value":"0","pk":"1896_summer","doctype":"g1896_summer","some_id":"cec17b83-bf1e-43e1-9ae0-e93e199944af"}
deleting the downloaded and wrangled files to save disk space...
done
```

Items to note:

1) Information about the files being uses, and the mappings applied, are logged. 
2) Information about the uploaded blob is logged.
3) Rows processed and processing elapses time is logged.
4) The first rows of both the input file and the output file are logged for visual verification of the transformation.

---

## Database-level Migration OmniScripts

As an alternative to manually executing these many granular generated scripts,
there are also **database-level OmniScripts** which will execute an end-to-end
migration (except for loading CosmosDB via ADF).

In short, they will execute the following:

- mongoexport raw data from the source database
- upload the raw mongoexport files
- wrangle the raw mongoexport data and upload the transformed data to Azure Blob storage
- optionally load CosmosDB using the mongoexport program
- optionally load CosmosDB using the DotNet loader program

### Validations

As an OmniScript executes, it will perform several validations before proceeding.
For example, it will first ensure that the necessary Azure Storage containers
exist.

And before loading CosmosDB via either mongoimport or the DotNet loader,
it will first ensure that the target CosmosDB and containers exist.

### env.sh

File **env.sh** contains these entries which govern the omniscripts:

```
# DB migration omniscript configuration
export M2C_OMNISCRIPT_DO_MONGOEXPORTS="yes"              # yes or no
export M2C_OMNISCRIPT_DO_MONGOEXPORT_UPLOADS="yes"       # yes or no
export M2C_OMNISCRIPT_MONGOEXPORT_UPLOAD_METHOD="python" # python or azcli
export M2C_OMNISCRIPT_DO_WRANGLE="yes"                   # yes or no
```

### Filenames

These generated omniscripts are named like the following:

```
migrate_db_olympics_omniscript.sh
migrate_db_openflights_omniscript.sh
```

### Sample OmniScript

A sample omniscript is shown here:

```
#!/bin/bash

# Bash shell script to execute a complete database migration (1)
# from mongoexport to CosmosDB loading, for a given source database.
#
# (1) = However, CosmosDB loading only when $M2C_COSMOS_LOAD_METHOD
# is either 'mongoimport' or 'dotnet_mongo_loader', and not 'adf'.
#
# This script will execute several other generated scripts.
# Set the several M2C_OMNISCRIPT_* variables, as necessary, in env.sh.
#
# Database Name: openflights
# Generated on:  2021-07-30 21:52:56 UTC
# Template:      migrate_db_omniscript.txt
# Use:
# ./migrate_db_openflights_omniscript.sh > tmp/migrate_db_openflights.txt

# define verification filenames:
verify_storage_containers_file="tmp/omniscript_openflights_storage_containers.json"
verify_wrangled_blobs_file="tmp/omniscript_openflights_wrangled_blobs.json"
verify_target_cosmos_db_file="tmp/omniscript_openflights_target_cosmos_db.json"
report_target_cosmos_db_file="tmp/omniscript_openflights_target_cosmos_db_report.json"

source ./env.sh

mkdir -p tmp
rm $verify_storage_containers_file
rm $verify_wrangled_blobs_file
rm $verify_target_cosmos_db_file
rm $report_target_cosmos_db_file

# -----------------------------------------------------------------------------

if [[ $M2C_OMNISCRIPT_DO_MONGOEXPORTS == "yes" ]];
then
    ./openflights_mongoexports.sh
fi

# -----------------------------------------------------------------------------

# Verify that the necessary Azure Storage Blob containers are present

source bin/activate
python --version

source env.sh ; python validate.py storage_containers openflights $verify_storage_containers_file 

if [[ -f "$verify_storage_containers_file" ]];
then
    echo 'Azure Storage Blob containers are present, proceeding...'
else
    echo 'TERMINATING - Azure Storage container(s) are absent'
    exit 1
fi

# -----------------------------------------------------------------------------

if [[ $M2C_OMNISCRIPT_DO_MONGOEXPORT_UPLOADS == "yes" ]];
then
    if [[ $M2C_OMNISCRIPT_MONGOEXPORT_UPLOAD_METHOD == "azcli" ]];
    then
        ./openflights_az_cli_mongoexport_uploads.sh
    else
        ./openflights_python_mongoexport_uploads.sh
    fi
fi

# -----------------------------------------------------------------------------

if [[ $M2C_OMNISCRIPT_DO_WRANGLE == "yes" ]];
then
    if [[ $M2C_COSMOS_LOAD_METHOD == "adf" ]]
    then
        # No need to verify the target CosmosDB yet
        ./wrangle_openflights_all.sh
    else
        # Verify the target CosmosDB since the Wrangle process will also load
        source env.sh ; python validate.py target_cosmos_db openflights $verify_target_cosmos_db_file 
        
        if [[ -f "$verify_target_cosmos_db_file" ]];
        then
            echo 'CosmosDB database and containers are present, proceeding...'
            ./wrangle_openflights_all.sh
        else
            echo 'TERMINATING - Wrangled blob(s) are absent'
            exit 2
        fi

        # Get CosmosDB document counts by collection
        source env.sh ; python validate.py target_cosmos_db openflights $report_target_cosmos_db_file
    fi
fi

echo 'done'
```

---

## Execute ADF Pipelines

The last steps of the migration process are to execute each ADF Pipeline.

This can be done either in the Azure Portal and ADF UI, or from a command-line
to execute the generated scripts.

**The purpose of these ADF Pipelines are to copy the transformed mongoexport files to the containers in your CosmosDB database.**

For example, the reference application produces these scripts.

```
adf_pipeline_copy_to_olympics_games.sh
adf_pipeline_copy_to_olympics_locations.sh
adf_pipeline_copy_to_travel_airlines.sh
adf_pipeline_copy_to_travel_airports.sh
adf_pipeline_copy_to_travel_countries.sh
adf_pipeline_copy_to_travel_planes.sh
adf_pipeline_copy_to_travel_routes.sh
```

Execute each script as follows:

```
$ ./adf_pipeline_copy_to_travel_routes.sh
Command group 'datafactory pipeline' is experimental and under development. Reference and support levels: https://aka.ms/CLI_refstatus
{
  "runId": "9512045e-cd4a-11eb-9923-acde48001122"
}
```

This gives you a **runId** that you can **then monitor in Azure Data Factory**.

Then **visit the Monitor tab of your ADF UI**, and verify that the Pipeline completes successfully.  Scroll to the right of the list of Pipeline Runs to see the **Run ID**
column.  Alternatively, enter the runID value in the search box at the top of the list.

#### ADF Monitor View with list of Pipeline Runs

<p align="center"><img src="img/adf-monitor-pipelines-list.png" width="99%"></p>

---

#### Search for Pipeline by runId

Enter the runId in the search box at the top of the list.

<p align="center"><img src="img/adf-pipeline-search-by-runid.png" width="99%"></p>

---

#### A completed Pipeline: travel routes

From the pipeline runs list, click into a Pipeline run to display its details.

<p align="center"><img src="img/adf-completed-pipeline-travel-routes.png" width="99%"></p>

---

#### A completed Pipeline: olympics games

<p align="center"><img src="img/adf-completed-pipeline-olympics-games.png" width="99%"></p>

---

## Validation

At any point in the migration you can execute a **validation process** to confirm 
that expected Storage Containers, Blobs, and CosmosDB databases and containers are
actually present.

For example, before you execute the wrangling scripts you'll want to verify
that the input blobs are present.

Likewise, before you execute the ADF pipelines you'll want to confirm that both 
the wrangled blobs and the target  CosmosDB databases and collections are present.

Here's a list of the available validations and how to execute them:

```
source env.sh ; python validate.py storage_containers
source env.sh ; python validate.py raw_blobs
source env.sh ; python validate.py wrangled_blobs
source env.sh ; python validate.py target_cosmos_db
source env.sh ; python validate.py all    <-- executes all of the above
```

### Sample Output 

```
$ source env.sh ; python validate.py all

validating all ...

validate_storage_containers ...
OK, container present: olympics-games-adf
OK, container present: olympics-locations-adf
OK, container present: olympics-raw
OK, container present: openflights-raw
OK, container present: travel-airlines-adf
OK, container present: travel-airports-adf
OK, container present: travel-countries-adf
OK, container present: travel-planes-adf
OK, container present: travel-routes-adf

validate_raw_blobs ...
OK, raw blob present; container: olympics-raw blob: olympics__countries.json size: 20365
OK, raw blob present; container: olympics-raw blob: olympics__g1896_summer.json size: 125037
OK, raw blob present; container: olympics-raw blob: olympics__g1900_summer.json size: 632359
OK, raw blob present; container: olympics-raw blob: olympics__g1904_summer.json size: 442391
OK, raw blob present; container: olympics-raw blob: olympics__g1906_summer.json size: 576820
OK, raw blob present; container: olympics-raw blob: olympics__g1908_summer.json size: 1024421
OK, raw blob present; container: olympics-raw blob: olympics__g1912_summer.json size: 1354740
OK, raw blob present; container: olympics-raw blob: olympics__g1920_summer.json size: 1435359
OK, raw blob present; container: olympics-raw blob: olympics__g1924_summer.json size: 1709472
OK, raw blob present; container: olympics-raw blob: olympics__g1924_winter.json size: 154737
OK, raw blob present; container: olympics-raw blob: olympics__g1928_summer.json size: 1667939
OK, raw blob present; container: olympics-raw blob: olympics__g1928_winter.json size: 196522
OK, raw blob present; container: olympics-raw blob: olympics__g1932_summer.json size: 1018258
OK, raw blob present; container: olympics-raw blob: olympics__g1932_winter.json size: 119721
OK, raw blob present; container: olympics-raw blob: olympics__g1936_summer.json size: 2136780
OK, raw blob present; container: olympics-raw blob: olympics__g1936_winter.json size: 310950
OK, raw blob present; container: olympics-raw blob: olympics__g1948_summer.json size: 2106381
OK, raw blob present; container: olympics-raw blob: olympics__g1948_winter.json size: 361857
OK, raw blob present; container: olympics-raw blob: olympics__g1952_summer.json size: 2735307
OK, raw blob present; container: olympics-raw blob: olympics__g1952_winter.json size: 358855
OK, raw blob present; container: olympics-raw blob: olympics__g1956_summer.json size: 1713391
OK, raw blob present; container: olympics-raw blob: olympics__g1956_winter.json size: 449058
OK, raw blob present; container: olympics-raw blob: olympics__g1960_summer.json size: 2677642
OK, raw blob present; container: olympics-raw blob: olympics__g1960_winter.json size: 382169
OK, raw blob present; container: olympics-raw blob: olympics__g1964_summer.json size: 2547116
OK, raw blob present; container: olympics-raw blob: olympics__g1964_winter.json size: 600251
OK, raw blob present; container: olympics-raw blob: olympics__g1968_summer.json size: 2900825
OK, raw blob present; container: olympics-raw blob: olympics__g1968_winter.json size: 638506
OK, raw blob present; container: olympics-raw blob: olympics__g1972_summer.json size: 3419187
OK, raw blob present; container: olympics-raw blob: olympics__g1972_winter.json size: 558672
OK, raw blob present; container: olympics-raw blob: olympics__g1976_summer.json size: 2887176
OK, raw blob present; container: olympics-raw blob: olympics__g1976_winter.json size: 628892
OK, raw blob present; container: olympics-raw blob: olympics__g1980_summer.json size: 2380176
OK, raw blob present; container: olympics-raw blob: olympics__g1980_winter.json size: 594809
OK, raw blob present; container: olympics-raw blob: olympics__g1984_summer.json size: 3174258
OK, raw blob present; container: olympics-raw blob: olympics__g1984_winter.json size: 722006
OK, raw blob present; container: olympics-raw blob: olympics__g1988_summer.json size: 3973001
OK, raw blob present; container: olympics-raw blob: olympics__g1988_winter.json size: 886867
OK, raw blob present; container: olympics-raw blob: olympics__g1992_summer.json size: 4328061
OK, raw blob present; container: olympics-raw blob: olympics__g1992_winter.json size: 1172426
OK, raw blob present; container: olympics-raw blob: olympics__g1994_winter.json size: 1083239
OK, raw blob present; container: olympics-raw blob: olympics__g1996_summer.json size: 4567620
OK, raw blob present; container: olympics-raw blob: olympics__g1998_winter.json size: 1216227
OK, raw blob present; container: olympics-raw blob: olympics__g2000_summer.json size: 4574295
OK, raw blob present; container: olympics-raw blob: olympics__g2002_winter.json size: 1417214
OK, raw blob present; container: olympics-raw blob: olympics__g2004_summer.json size: 4447320
OK, raw blob present; container: olympics-raw blob: olympics__g2006_winter.json size: 1475181
OK, raw blob present; container: olympics-raw blob: olympics__g2008_summer.json size: 4511678
OK, raw blob present; container: olympics-raw blob: olympics__g2010_winter.json size: 1497220
OK, raw blob present; container: olympics-raw blob: olympics__g2012_summer.json size: 4273943
OK, raw blob present; container: olympics-raw blob: olympics__g2014_winter.json size: 1639687
OK, raw blob present; container: olympics-raw blob: olympics__g2016_summer.json size: 4624209
OK, raw blob present; container: olympics-raw blob: olympics__games.json size: 4309
OK, raw blob present; container: openflights-raw blob: openflights__airlines.json size: 1140892
OK, raw blob present; container: openflights-raw blob: openflights__airports.json size: 2691581
OK, raw blob present; container: openflights-raw blob: openflights__countries.json size: 25621
OK, raw blob present; container: openflights-raw blob: openflights__planes.json size: 24399
OK, raw blob present; container: openflights-raw blob: openflights__routes.json size: 16384309

validate_wrangled_blobs ...
OK, blob present; container: olympics-locations-adf blob: olympics__countries__wrangled.json size: 34165 adf/raw size ratio: 1.6776331942057452
OK, blob present; container: olympics-games-adf blob: olympics__g1896_summer__wrangled.json size: 155348 adf/raw size ratio: 1.2424162447915417
OK, blob present; container: olympics-games-adf blob: olympics__g1900_summer__wrangled.json size: 786885 adf/raw size ratio: 1.2443643563229114
OK, blob present; container: olympics-games-adf blob: olympics__g1904_summer__wrangled.json size: 546118 adf/raw size ratio: 1.2344690556543871
OK, blob present; container: olympics-games-adf blob: olympics__g1906_summer__wrangled.json size: 715085 adf/raw size ratio: 1.2397021601192746
OK, blob present; container: olympics-games-adf blob: olympics__g1908_summer__wrangled.json size: 1271939 adf/raw size ratio: 1.2416174600091174
OK, blob present; container: olympics-games-adf blob: olympics__g1912_summer__wrangled.json size: 1677229 adf/raw size ratio: 1.2380449385121868
OK, blob present; container: olympics-games-adf blob: olympics__g1920_summer__wrangled.json size: 1777915 adf/raw size ratio: 1.2386552771815273
OK, blob present; container: olympics-games-adf blob: olympics__g1924_summer__wrangled.json size: 2127098 adf/raw size ratio: 1.2443011643361226
OK, blob present; container: olympics-games-adf blob: olympics__g1924_winter__wrangled.json size: 191436 adf/raw size ratio: 1.2371701661528918
OK, blob present; container: olympics-games-adf blob: olympics__g1928_summer__wrangled.json size: 2066252 adf/raw size ratio: 1.2388054958844419
OK, blob present; container: olympics-games-adf blob: olympics__g1928_winter__wrangled.json size: 242969 adf/raw size ratio: 1.2363450402499465
OK, blob present; container: olympics-games-adf blob: olympics__g1932_summer__wrangled.json size: 1255236 adf/raw size ratio: 1.2327288368959537
OK, blob present; container: olympics-games-adf blob: olympics__g1932_winter__wrangled.json size: 147802 adf/raw size ratio: 1.234553670617519
OK, blob present; container: olympics-games-adf blob: olympics__g1936_summer__wrangled.json size: 2655920 adf/raw size ratio: 1.2429543518752515
OK, blob present; container: olympics-games-adf blob: olympics__g1936_winter__wrangled.json size: 382359 adf/raw size ratio: 1.229647853352629
OK, blob present; container: olympics-games-adf blob: olympics__g1948_summer__wrangled.json size: 2617628 adf/raw size ratio: 1.2427134502257664
OK, blob present; container: olympics-games-adf blob: olympics__g1948_winter__wrangled.json size: 447683 adf/raw size ratio: 1.2371820912680975
OK, blob present; container: olympics-games-adf blob: olympics__g1952_summer__wrangled.json size: 3395222 adf/raw size ratio: 1.24125811106395
OK, blob present; container: olympics-games-adf blob: olympics__g1952_winter__wrangled.json size: 445705 adf/raw size ratio: 1.2420197572835825
OK, blob present; container: olympics-games-adf blob: olympics__g1956_summer__wrangled.json size: 2122418 adf/raw size ratio: 1.2387236771991916
OK, blob present; container: olympics-games-adf blob: olympics__g1956_winter__wrangled.json size: 553392 adf/raw size ratio: 1.2323396977673262
OK, blob present; container: olympics-games-adf blob: olympics__g1960_summer__wrangled.json size: 3325801 adf/raw size ratio: 1.2420633527558949
OK, blob present; container: olympics-games-adf blob: olympics__g1960_winter__wrangled.json size: 471215 adf/raw size ratio: 1.233001630168852
OK, blob present; container: olympics-games-adf blob: olympics__g1964_summer__wrangled.json size: 3161868 adf/raw size ratio: 1.241352180269764
OK, blob present; container: olympics-games-adf blob: olympics__g1964_winter__wrangled.json size: 742111 adf/raw size ratio: 1.2363344667480771
OK, blob present; container: olympics-games-adf blob: olympics__g1968_summer__wrangled.json size: 3586413 adf/raw size ratio: 1.2363424198288417
OK, blob present; container: olympics-games-adf blob: olympics__g1968_winter__wrangled.json size: 789426 adf/raw size ratio: 1.2363642628260345
OK, blob present; container: olympics-games-adf blob: olympics__g1972_summer__wrangled.json size: 4241646 adf/raw size ratio: 1.240542269258745
OK, blob present; container: olympics-games-adf blob: olympics__g1972_winter__wrangled.json size: 690712 adf/raw size ratio: 1.236346192399118
OK, blob present; container: olympics-games-adf blob: olympics__g1976_summer__wrangled.json size: 3576833 adf/raw size ratio: 1.2388690540514329
OK, blob present; container: olympics-games-adf blob: olympics__g1976_winter__wrangled.json size: 777372 adf/raw size ratio: 1.236097771954485
OK, blob present; container: olympics-games-adf blob: olympics__g1980_summer__wrangled.json size: 2954222 adf/raw size ratio: 1.2411779633102762
OK, blob present; container: olympics-games-adf blob: olympics__g1980_winter__wrangled.json size: 734144 adf/raw size ratio: 1.2342516673419535
OK, blob present; container: olympics-games-adf blob: olympics__g1984_summer__wrangled.json size: 3929032 adf/raw size ratio: 1.237779663782843
OK, blob present; container: olympics-games-adf blob: olympics__g1984_winter__wrangled.json size: 892267 adf/raw size ratio: 1.235816599862051
OK, blob present; container: olympics-games-adf blob: olympics__g1988_summer__wrangled.json size: 4933977 adf/raw size ratio: 1.2418766066255709
OK, blob present; container: olympics-games-adf blob: olympics__g1988_winter__wrangled.json size: 1097418 adf/raw size ratio: 1.2374098934789546
OK, blob present; container: olympics-games-adf blob: olympics__g1992_summer__wrangled.json size: 5363845 adf/raw size ratio: 1.239318253601324
OK, blob present; container: olympics-games-adf blob: olympics__g1992_winter__wrangled.json size: 1446662 adf/raw size ratio: 1.2339047411094601
OK, blob present; container: olympics-games-adf blob: olympics__g1994_winter__wrangled.json size: 1335427 adf/raw size ratio: 1.2328091953853213
OK, blob present; container: olympics-games-adf blob: olympics__g1996_summer__wrangled.json size: 5667496 adf/raw size ratio: 1.240798490242183
OK, blob present; container: olympics-games-adf blob: olympics__g1998_winter__wrangled.json size: 1503860 adf/raw size ratio: 1.2364961475119365
OK, blob present; container: olympics-games-adf blob: olympics__g2000_summer__wrangled.json size: 5677390 adf/raw size ratio: 1.2411508221485497
OK, blob present; container: olympics-games-adf blob: olympics__g2002_winter__wrangled.json size: 1745080 adf/raw size ratio: 1.2313454425372596
OK, blob present; container: olympics-games-adf blob: olympics__g2004_summer__wrangled.json size: 5520144 adf/raw size ratio: 1.2412293246269663
OK, blob present; container: olympics-games-adf blob: olympics__g2006_winter__wrangled.json size: 1824854 adf/raw size ratio: 1.2370373533823984
OK, blob present; container: olympics-games-adf blob: olympics__g2008_summer__wrangled.json size: 5597199 adf/raw size ratio: 1.240602498671226
OK, blob present; container: olympics-games-adf blob: olympics__g2010_winter__wrangled.json size: 1848380 adf/raw size ratio: 1.2345413499686084
OK, blob present; container: olympics-games-adf blob: olympics__g2012_summer__wrangled.json size: 5305226 adf/raw size ratio: 1.2412954501264992
OK, blob present; container: olympics-games-adf blob: olympics__g2014_winter__wrangled.json size: 2029927 adf/raw size ratio: 1.2379966420420483
OK, blob present; container: olympics-games-adf blob: olympics__g2016_summer__wrangled.json size: 5716830 adf/raw size ratio: 1.2362827891213395
OK, blob present; container: olympics-locations-adf blob: olympics__games__wrangled.json size: 7777 adf/raw size ratio: 1.8048271060570897
OK, blob present; container: travel-airlines-adf blob: openflights__airlines__wrangled.json size: 1296479 adf/raw size ratio: 1.1363731185773938
OK, blob present; container: travel-airports-adf blob: openflights__airports__wrangled.json size: 2930510 adf/raw size ratio: 1.0887690171687199
OK, blob present; container: travel-countries-adf blob: openflights__countries__wrangled.json size: 30345 adf/raw size ratio: 1.1843800007806096
OK, blob present; container: travel-planes-adf blob: openflights__planes__wrangled.json size: 30899 adf/raw size ratio: 1.2664043608344604
OK, blob present; container: travel-routes-adf blob: openflights__routes__wrangled.json size: 18697344 adf/raw size ratio: 1.1411737901183383

validate_target_cosmos_db ...
OK, MongoClient created
OK, collection 'games' is in database 'olympics'
OK, collection 'locations' is in database 'olympics'
OK, collection 'airlines' is in database 'travel'
OK, collection 'airports' is in database 'travel'
OK, collection 'countries' is in database 'travel'
OK, collection 'planes' is in database 'travel'
OK, collection 'routes' is in database 'travel'
```

Note: if you execute validate.py with the **all** option it will calculate,
and additionally display, the ratio of the wrangled blob size vs the corresponding
raw blob size.
