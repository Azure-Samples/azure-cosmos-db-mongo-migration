#!/bin/bash

# bash script to execute the mongoimport program to load the reference database
# with the sample data provided in this repo.
# Chris Joakim, Microsoft, October 2021

source env.sh

echo 'database URL: '$DOCKER_MONGODB_URL

echo 'init database ...'
mongo -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS $DOCKER_MONGODB_URL/admin < mongo/olympics_init.ddl

echo 'sleeping 10 after init database...'
sleep 10

echo 'mongoimport countries ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection countries \
    --file olympics/import_json/countries.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1896_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1896_summer \
    --file olympics/import_json/g1896_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1900_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1900_summer \
    --file olympics/import_json/g1900_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1904_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1904_summer \
    --file olympics/import_json/g1904_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1906_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1906_summer \
    --file olympics/import_json/g1906_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1908_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1908_summer \
    --file olympics/import_json/g1908_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1912_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1912_summer \
    --file olympics/import_json/g1912_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1920_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1920_summer \
    --file olympics/import_json/g1920_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1924_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1924_summer \
    --file olympics/import_json/g1924_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1924_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1924_winter \
    --file olympics/import_json/g1924_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1928_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1928_summer \
    --file olympics/import_json/g1928_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1928_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1928_winter \
    --file olympics/import_json/g1928_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1932_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1932_summer \
    --file olympics/import_json/g1932_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1932_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1932_winter \
    --file olympics/import_json/g1932_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1936_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1936_summer \
    --file olympics/import_json/g1936_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1936_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1936_winter \
    --file olympics/import_json/g1936_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1948_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1948_summer \
    --file olympics/import_json/g1948_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1948_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1948_winter \
    --file olympics/import_json/g1948_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1952_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1952_summer \
    --file olympics/import_json/g1952_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1952_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1952_winter \
    --file olympics/import_json/g1952_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1956_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1956_summer \
    --file olympics/import_json/g1956_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1956_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1956_winter \
    --file olympics/import_json/g1956_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1960_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1960_summer \
    --file olympics/import_json/g1960_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1960_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1960_winter \
    --file olympics/import_json/g1960_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1964_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1964_summer \
    --file olympics/import_json/g1964_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1964_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1964_winter \
    --file olympics/import_json/g1964_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1968_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1968_summer \
    --file olympics/import_json/g1968_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1968_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1968_winter \
    --file olympics/import_json/g1968_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1972_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1972_summer \
    --file olympics/import_json/g1972_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1972_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1972_winter \
    --file olympics/import_json/g1972_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1976_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1976_summer \
    --file olympics/import_json/g1976_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1976_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1976_winter \
    --file olympics/import_json/g1976_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1980_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1980_summer \
    --file olympics/import_json/g1980_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1980_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1980_winter \
    --file olympics/import_json/g1980_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1984_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1984_summer \
    --file olympics/import_json/g1984_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1984_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1984_winter \
    --file olympics/import_json/g1984_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1988_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1988_summer \
    --file olympics/import_json/g1988_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1988_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1988_winter \
    --file olympics/import_json/g1988_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1992_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1992_summer \
    --file olympics/import_json/g1992_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1992_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1992_winter \
    --file olympics/import_json/g1992_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1994_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1994_winter \
    --file olympics/import_json/g1994_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1996_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1996_summer \
    --file olympics/import_json/g1996_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g1998_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1998_winter \
    --file olympics/import_json/g1998_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g2000_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g2000_summer \
    --file olympics/import_json/g2000_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g2002_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g2002_winter \
    --file olympics/import_json/g2002_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g2004_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g2004_summer \
    --file olympics/import_json/g2004_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g2006_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g2006_winter \
    --file olympics/import_json/g2006_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g2008_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g2008_summer \
    --file olympics/import_json/g2008_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g2010_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g2010_winter \
    --file olympics/import_json/g2010_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g2012_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g2012_summer \
    --file olympics/import_json/g2012_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g2014_winter ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g2014_winter \
    --file olympics/import_json/g2014_winter.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport g2016_summer ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g2016_summer \
    --file olympics/import_json/g2016_summer.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'mongoimport games ...'
mongoimport --authenticationDatabase admin -u $DOCKER_MONGODB_USER -p $DOCKER_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection games \
    --file olympics/import_json/games.json \
    --numInsertionWorkers 1 \
    --batchSize 24  # no --ssl

echo 'done'