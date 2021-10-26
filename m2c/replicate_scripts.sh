#!/bin/bash

# Copy/Replicate the necessary scripts in this directory to the 
# generated shell scripts directory.
# Chris Joakim, Microsoft, July 2021

source env.sh

mkdir -p $M2C_APP_DIR
mkdir -p $M2C_APP_ARTIFACTS_DIR/adf
mkdir -p $M2C_APP_ARTIFACTS_DIR/shell
mkdir -p $M2C_APP_ARTIFACTS_DIR/shell/pysrc

echo 'copying to '$M2C_APP_ARTIFACTS_DIR'/shell ...'
cp env.sh         $M2C_APP_ARTIFACTS_DIR/shell
cp mongo_cli.sh   $M2C_APP_ARTIFACTS_DIR/shell
cp requirements*  $M2C_APP_ARTIFACTS_DIR/shell
cp storage.py     $M2C_APP_ARTIFACTS_DIR/shell
cp wrangle.py     $M2C_APP_ARTIFACTS_DIR/shell
cp validate.py    $M2C_APP_ARTIFACTS_DIR/shell
cp pysrc/*.py     $M2C_APP_ARTIFACTS_DIR/shell/pysrc

cp validate_original.py $M2C_APP_ARTIFACTS_DIR/shell

echo 'copying the mapping file(s) ...'
cp $M2C_APP_DATA_DIR/metadata/*_mapping.json $M2C_APP_ARTIFACTS_DIR/shell

echo 'done'
