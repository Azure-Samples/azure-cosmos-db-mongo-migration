#!/bin/bash

# Bash script with AZ CLI to automate the creation/deletion of an
# Azure Cosmos/Mongo DB.
# Chris Joakim, Microsoft, July 2021
#
# See https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest
# See https://docs.microsoft.com/en-us/azure/cosmos-db/scripts/cli/mongodb/create

# az login

source ./azconfig.sh

arg_count=$#
processed=0

mkdir -p tmp

create() {
    processed=1
    echo 'creating cosmos rg: '$cosmos_mongo_rg
    az group create \
        --location $cosmos_mongo_region \
        --name $cosmos_mongo_rg \
        --subscription $subscription \
        > tmp/cosmos_mongo_rg_create.json

    echo 'creating cosmos acct: '$cosmos_mongo_acct_name
    az cosmosdb create \
        --name $cosmos_mongo_acct_name \
        --resource-group $cosmos_mongo_rg \
        --subscription $subscription \
        --kind MongoDB \
        --server-version $cosmos_mongo_version \
        --default-consistency-level Eventual \
        --locations regionName=$cosmos_mongo_region isZoneRedundant=False \
        --enable-analytical-storage true \
        --enable-multiple-write-locations true \
        > tmp/cosmos_mongo_acct_create.json
}

info() {
    processed=1
    echo 'az cosmosdb show ...'
    az cosmosdb show \
        --name $cosmos_mongo_acct_name \
        --resource-group $cosmos_mongo_rg \
        > tmp/cosmos_mongo_db_show.json

    echo 'az cosmosdb keys list - keys ...'
    az cosmosdb keys list \
        --resource-group $cosmos_mongo_rg \
        --name $cosmos_mongo_acct_name \
        --type keys \
        > tmp/cosmos_mongo_db_keys.json

    echo 'az cosmosdb keys list - connection-strings ...'
    az cosmosdb keys list \
        --resource-group $cosmos_mongo_rg \
        --name $cosmos_mongo_acct_name \
        --type connection-strings \
        > tmp/cosmos_mongo_db_connection_strings.json
}

display_usage() {
    echo 'Usage:'
    echo './cosmos_mongo.sh create'
    echo './cosmos_mongo.sh info'
}

# ========== "main" logic below ==========

if [ $arg_count -gt 0 ]
then
    for arg in $@
    do
        if [ $arg == "create" ]; then create; fi 
        if [ $arg == "info" ];   then info; fi 
    done
fi

if [ $processed -eq 0 ]; then display_usage; fi

echo 'done'
