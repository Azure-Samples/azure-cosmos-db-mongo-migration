#!/bin/bash

# Bash shell script to download a raw mongoexport blob, transform it, 
# then import the transformed file to CosmosDB.
#
# Database Name: olympics
# Generated on:  2021-10-26 19:28:57 UTC
# Template:      wrangle_one_blob.txt

source ./env.sh

mkdir -p tmp/olympics/out
mkdir -p out/olympics

python wrangle.py transform_blob \
    --db olympics \
    --source-coll  games \
    --in-container olympics-raw \
    --blobname olympics__games.json \
    --filename tmp/olympics/olympics__games.json \
    --outfile  tmp/olympics/olympics__games__wrangled.json \
    --out-container olympics-locations-adf $1 $2 $3 

echo ''
echo 'first line of input file: tmp/olympics/olympics__games.json'
head -1 tmp/olympics/olympics__games.json

echo ''
echo 'first line of output file: tmp/olympics/olympics__games__wrangled.json'
head -1 tmp/olympics/olympics__games__wrangled.json

if [[ $M2C_COSMOS_LOAD_METHOD == "mongoimport" ]];
then
    echo ''
    echo 'executing mongoimport to db: olympics coll: locations ...' 

    mongoimport \
        --uri $M2C_COSMOS_MONGO_CONN_STRING \
        --db olympics \
        --collection locations \
        --file tmp/olympics/olympics__games__wrangled.json \
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
    echo 'executing dotnet_mongo_loader to db: olympics coll: locations ...' 

    dotnet run --project dotnet_mongo_loader/dotnet_mongo_loader.csproj \
        olympics locations tmp/olympics/olympics__games__wrangled.json \
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
    rm tmp/olympics/olympics__games.json
    rm tmp/olympics/olympics__games__wrangled.json
fi

echo 'done'