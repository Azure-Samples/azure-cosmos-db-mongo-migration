#!/bin/bash

# Bash script to generate the initial scripts to enable the fetching
# of source-database metadata.  Uses the list of databases in simple
# text file 'migrated_databases_list.txt'
# Chris Joakim, Microsoft, July 2021

source env.sh

./create_directories.sh

python main.py generate_initial_scripts

chmod 744 *.sh  # make them executable

echo 'done'
