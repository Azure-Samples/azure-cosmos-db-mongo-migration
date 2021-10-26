#!/bin/bash

# bash script to execute the mongoimport program to load the reference database
# with the sample data provided in this repo.
# Chris Joakim, Microsoft, October 2021

source env.sh

echo 'database URL: '$DOCKER_MONGODB_URL

echo 'init database ...'
mongo -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS $DOCKER_MONGODB_URL/admin < mongo/openflights_init.ddl

echo 'sleeping 10 after init database...'
sleep 10

echo 'mongoimport airlines ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db openflights \
    --collection airlines \
    --file openflights/import_json/airlines.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport airports ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db openflights \
    --collection airports \
    --file openflights/import_json/airports.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport countries ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db openflights \
    --collection countries \
    --file openflights/import_json/countries.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport planes ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db openflights \
    --collection planes \
    --file openflights/import_json/planes.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport routes ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db openflights \
    --collection routes \
    --file openflights/import_json/routes.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl


echo 'done'