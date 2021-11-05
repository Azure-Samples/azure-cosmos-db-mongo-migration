#!/bin/bash

# Bash script to execute the mongoexport_docsize_analyze.py Python script
# to do an analysis of a mongoexport file min/max/average document sizes.
# Chris Joakim, Microsoft, November 2021

source env.sh

# manually edit 'infile', on the next line:
export infile=$M2C_APP_DATA_DIR/mongoexports/openflights/openflights__routes.json

python mongoexport_docsize_analyze.py docsize_extract  $infile

python mongoexport_docsize_analyze.py docsize_analysis

echo 'done'
