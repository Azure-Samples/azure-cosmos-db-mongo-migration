#!/bin/bash

# Bash shell script to download a raw mongoexport blob, transform it, 
# then import the transformed file to CosmosDB.
#
# Database Name: openflights
# Generated on:  2021-10-26 19:28:58 UTC
# Template:      wrangle_one_blob.txt

source ./env.sh

mkdir -p tmp/openflights/out
mkdir -p out/openflights

python wrangle.py transform_blob \
    --db openflights \
    --source-coll  airports \
    --in-container openflights-raw \
    --blobname openflights__airports.json \
    --filename tmp/openflights/openflights__airports.json \
    --outfile  tmp/openflights/openflights__airports__wrangled.json \
    --out-container travel-airports-adf $1 $2 $3 

echo ''
echo 'first line of input file: tmp/openflights/openflights__airports.json'
head -1 tmp/openflights/openflights__airports.json

echo ''
echo 'first line of output file: tmp/openflights/openflights__airports__wrangled.json'
head -1 tmp/openflights/openflights__airports__wrangled.json

if [[ $M2C_COSMOS_LOAD_METHOD == "mongoimport" ]];
then
    echo ''
    echo 'executing mongoimport to db: travel coll: airports ...' 

    mongoimport \
        --uri $M2C_COSMOS_MONGO_CONN_STRING \
        --db travel \
        --collection airports \
        --file tmp/openflights/openflights__airports__wrangled.json \
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
    echo 'executing dotnet_mongo_loader to db: travel coll: airports ...' 

    dotnet run --project dotnet_mongo_loader/dotnet_mongo_loader.csproj \
        travel airports tmp/openflights/openflights__airports__wrangled.json \
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
    rm tmp/openflights/openflights__airports.json
    rm tmp/openflights/openflights__airports__wrangled.json
fi

echo 'done'