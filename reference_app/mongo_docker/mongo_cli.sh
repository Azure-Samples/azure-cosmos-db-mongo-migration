#!/bin/bash

# Bash script to connect to a mongodb database with the mongo cli program.
# Set environment variable AZURE_COSMOSDB_MONGODB_CONN_STRING to connect
# to Azure CosmosDB.
# Chris Joakim, Microsoft, October 2021

source env.sh

if [ "$1" == 'local' ]
then 
    echo 'connecting to '$DOCKER_MONGODB_URL
    mongo admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS
fi

if [ "$1" == 'azure' ]
then 
    echo 'connecting to '$AZURE_COSMOSDB_MONGODB_CONN_STRING
    mongo $AZURE_COSMOSDB_MONGODB_CONN_STRING --ssl
fi
