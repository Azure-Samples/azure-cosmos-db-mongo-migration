#!/bin/bash

# Bash script to execute the mongoexport_analyze.py Python script
# to do an analysis of a mongoexport file for potential partition keys
# Chris Joakim, Microsoft, October 2021

source env.sh

export infile=$M2C_APP_DATA_DIR/mongoexports/openflights/openflights__routes.json

python mongoexport_pk_analyze.py pk_analysis $infile

echo 'done'
