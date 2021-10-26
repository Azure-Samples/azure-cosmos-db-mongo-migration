#!/bin/bash

# Bash shell script to upload mongoexport blobs to Azure Storage with the az CLI.
#
# Database Name: openflights
# Generated on:  2021-10-26 19:28:58 UTC
# Generated by:  artifact_generator.py gen_az_cli_uploads()
# Template:      blob_uploads_az_cli.txt

source env.sh

# Uncomment as necessary:
# echo 'acct: '$M2C_STORAGE_ACCOUNT
# echo 'key:  '$M2C_STORAGE_KEY


echo '---'
echo 'uploading /Users/cjoakim/github/azure-cosmos-db-mongo-migration/reference_app/data/mongoexports/openflights/openflights__airlines.json to openflights-raw ...'
date 
az storage blob upload \
  --container-name openflights-raw \
  --file /Users/cjoakim/github/azure-cosmos-db-mongo-migration/reference_app/data/mongoexports/openflights/openflights__airlines.json \
  --name  openflights__airlines.json \
  --account-name $M2C_STORAGE_ACCOUNT \
  --account-key $M2C_STORAGE_KEY

echo '---'
echo 'uploading /Users/cjoakim/github/azure-cosmos-db-mongo-migration/reference_app/data/mongoexports/openflights/openflights__airports.json to openflights-raw ...'
date 
az storage blob upload \
  --container-name openflights-raw \
  --file /Users/cjoakim/github/azure-cosmos-db-mongo-migration/reference_app/data/mongoexports/openflights/openflights__airports.json \
  --name  openflights__airports.json \
  --account-name $M2C_STORAGE_ACCOUNT \
  --account-key $M2C_STORAGE_KEY

echo '---'
echo 'uploading /Users/cjoakim/github/azure-cosmos-db-mongo-migration/reference_app/data/mongoexports/openflights/openflights__countries.json to openflights-raw ...'
date 
az storage blob upload \
  --container-name openflights-raw \
  --file /Users/cjoakim/github/azure-cosmos-db-mongo-migration/reference_app/data/mongoexports/openflights/openflights__countries.json \
  --name  openflights__countries.json \
  --account-name $M2C_STORAGE_ACCOUNT \
  --account-key $M2C_STORAGE_KEY

echo '---'
echo 'uploading /Users/cjoakim/github/azure-cosmos-db-mongo-migration/reference_app/data/mongoexports/openflights/openflights__planes.json to openflights-raw ...'
date 
az storage blob upload \
  --container-name openflights-raw \
  --file /Users/cjoakim/github/azure-cosmos-db-mongo-migration/reference_app/data/mongoexports/openflights/openflights__planes.json \
  --name  openflights__planes.json \
  --account-name $M2C_STORAGE_ACCOUNT \
  --account-key $M2C_STORAGE_KEY

echo '---'
echo 'uploading /Users/cjoakim/github/azure-cosmos-db-mongo-migration/reference_app/data/mongoexports/openflights/openflights__routes.json to openflights-raw ...'
date 
az storage blob upload \
  --container-name openflights-raw \
  --file /Users/cjoakim/github/azure-cosmos-db-mongo-migration/reference_app/data/mongoexports/openflights/openflights__routes.json \
  --name  openflights__routes.json \
  --account-name $M2C_STORAGE_ACCOUNT \
  --account-key $M2C_STORAGE_KEY


date

#echo ''
#echo 'listing contents of container: openflights-raw'
#az storage blob list -c openflights-raw \
#  --auth-mode key \
#  --account-name $M2C_STORAGE_ACCOUNT \
#  --account-key $M2C_STORAGE_KEY

echo 'done'