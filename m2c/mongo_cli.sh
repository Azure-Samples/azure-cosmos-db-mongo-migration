#!/bin/bash

# Bash script to connect to a MongoDB database with the mongo cli program.
# Use:
# $ ./mongo_cli.sh local
# $ ./mongo_cli.sh azure
# Chris Joakim, Microsoft, July 2021

source env.sh

if [ "$1" == 'local' ]
then 
    echo 'Connecting to local containerized MongoDB'
    echo 'see https://github.com/cjoakim/azure-m2c-wgm-reference-app'
    mongo admin -u $M2C_SOURCE_MONGODB_USER -p $M2C_SOURCE_MONGODB_PASS
fi

if [ "$1" == 'azure' ]
then 
    echo 'Connecting to CosmosDB: '$AZURE_COSMOSDB_MONGODB_CONN_STRING
    mongo $M2C_COSMOS_MONGO_CONN_STRING --ssl
fi
