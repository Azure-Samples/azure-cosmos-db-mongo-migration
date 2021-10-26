#!/bin/bash

# Bash script to demonstrate, in one script, the process to
# extract metadata, create mappings, and generate artifacts.
# Chris Joakim, Microsoft, July 2021

source env.sh

# Run this once:
# echo 'creating python virtual environment (see requirements txt files) ...'
# ./venv.sh create
# - or -
# ./pyenv.sh

echo 'displaying python libraries in this virtual environment'
pip list

echo ''
read -p 'Press enter to display env.sh'
cat env.sh

echo ''
read -p 'Press enter to display migrated_databases_list.txt'
cat $M2C_APP_DATA_DIR/metadata/migrated_databases_list.txt

echo ''
read -p 'Press enter to create directories (in $M2C_APP_DIR)'
create_directories.sh

echo ''
read -p 'Press enter to generate initial scripts'
./generate_initial_scripts.sh

echo ''
read -p 'Press enter to extract source database metadata'
./extract_metadata.sh

echo ''
read -p 'Press enter to generate mapping files'
./generate_mapping_files.sh

echo ''
read -p 'Press enter to generate manifest file from (metadata and mappings)'
./generate_manifest.sh

echo ''
read -p 'Press enter to generate artifacts'
./generate_artifacts.sh
