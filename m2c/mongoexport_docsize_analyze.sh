#!/bin/bash

# Bash script to execute the mongoexport_docsize_analyze.py Python script
# to do an analysis of a mongoexport file min/max/average document sizes.
# Chris Joakim, Microsoft, November 2021

source env.sh

mkdir -p tmp/

# manually edit 'infile', on the next line:
export infile=$M2C_APP_DATA_DIR/mongoexports/olympics/olympics__g2016_summer.json

python mongoexport_docsize_analyze.py docsize_extract $infile > tmp/docsize_extract.csv

echo 'head of file tmp/docsize_extract.csv:'
head  tmp/docsize_extract.csv

python mongoexport_docsize_analyze.py docsize_analysis

echo 'done'

# Sample Output:
# $ ./mongoexport_docsize_analyze.sh
# docsize_extract: /Users/cjoakim/github/azure-cosmos-db-mongo-migration/reference_app/data/mongoexports/olympics/olympics__g2016_summer.json
# max_doc_size: 2097152
# head of file tmp/docsize_extract.csv:
# row_index,doc_size,large_ind
# 0,340,0
# 1,330,0
# 2,343,0
# 3,341,0
# 4,347,0
# 5,330,0
# 6,337,0
# 7,345,0
# 8,323,0
# docsize_analysis: tmp/docsize_extract.csv
# row/doc count:   13688
# large doc count: 0
# max doc size:    387
# avg doc size:    336.8294126241964
# min doc size:    306
# done
