#!/bin/bash

# Bash and python script to wrangle the raw data files in the openflights/raw/
# directory into mongoimport files in the openflights/import_json/ directory.
# Users of this repo don't need to execute this script, as the output files
# are already present in the openflights/import_json/ directory.
# Chris Joakim, Microsoft, October 2021

mkdir -p tmp

echo 'airports ...'
python main.py parse_openflights_data airports  > ../openflights/import_json/airports.json
wc ../openflights/raw/airports.dat
wc ../openflights/import_json/airports.json

echo 'airlines ...'
python main.py parse_openflights_data airlines  > ../openflights/import_json/airlines.json
wc ../openflights/raw/airlines.dat
wc ../openflights/import_json/airlines.json

echo 'routes ...'
python main.py parse_openflights_data routes    > ../openflights/import_json/routes.json
wc ../openflights/raw/routes.dat
wc ../openflights/import_json/routes.json

echo 'planes ...'
python main.py parse_openflights_data planes    > ../openflights/import_json/planes.json
wc ../openflights/raw/planes.dat
wc ../openflights/import_json/planes.json

echo 'countries ...'
python main.py parse_openflights_data countries > ../openflights/import_json/countries.json
wc ../openflights/raw/countries.dat
wc ../openflights/import_json/countries.json

echo 'done'
