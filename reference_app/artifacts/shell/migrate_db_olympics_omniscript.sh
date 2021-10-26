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
# Database Name: olympics
# Generated on:  2021-10-26 19:28:57 UTC
# Template:      migrate_db_omniscript.txt
# Use:
# ./migrate_db_olympics_omniscript.sh > tmp/migrate_db_olympics.txt

# define verification filenames:
verify_storage_containers_file="tmp/omniscript_olympics_storage_containers.json"
verify_wrangled_blobs_file="tmp/omniscript_olympics_wrangled_blobs.json"
verify_target_cosmos_db_file="tmp/omniscript_olympics_target_cosmos_db.json"
report_target_cosmos_db_file="tmp/omniscript_olympics_target_cosmos_db_report.json"

source ./env.sh

mkdir -p tmp
rm $verify_storage_containers_file
rm $verify_wrangled_blobs_file
rm $verify_target_cosmos_db_file
rm $report_target_cosmos_db_file

# -----------------------------------------------------------------------------

if [[ $M2C_OMNISCRIPT_DO_MONGOEXPORTS == "yes" ]];
then
    ./olympics_mongoexports.sh
fi

# -----------------------------------------------------------------------------

# Verify that the necessary Azure Storage Blob containers are present

source bin/activate
python --version

source env.sh ; python validate.py storage_containers olympics $verify_storage_containers_file 

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
        ./olympics_az_cli_mongoexport_uploads.sh
    else
        ./olympics_python_mongoexport_uploads.sh
    fi
fi

# -----------------------------------------------------------------------------

if [[ $M2C_OMNISCRIPT_DO_WRANGLE == "yes" ]];
then
    if [[ $M2C_COSMOS_LOAD_METHOD == "adf" ]]
    then
        # No need to verify the target CosmosDB yet
        ./wrangle_olympics_all.sh
    else
        # Verify the target CosmosDB since the Wrangle process will also load
        source env.sh ; python validate.py target_cosmos_db olympics $verify_target_cosmos_db_file 
        
        if [[ -f "$verify_target_cosmos_db_file" ]];
        then
            echo 'CosmosDB database and containers are present, proceeding...'
            ./wrangle_olympics_all.sh
        else
            echo 'TERMINATING - Wrangled blob(s) are absent'
            exit 2
        fi

        # Get CosmosDB document counts by collection
        source env.sh ; python validate.py target_cosmos_db olympics $report_target_cosmos_db_file
    fi
fi

echo 'done'