#!/bin/bash

# Bash shell script to wrangle/transform a raw mongoexport file
#
# Database Name: openflights
# Generated on:  2021-10-26 19:28:58 UTC
# Template:      wrangle_all.txt

source ./env.sh

skip_download_flag=""  # set to "--skip-download" to bypass blob downloading


echo 'executing wrangle_openflights_airlines.sh ...'
./wrangle_openflights_airlines.sh $skip_download_flag

echo 'executing wrangle_openflights_airports.sh ...'
./wrangle_openflights_airports.sh $skip_download_flag

echo 'executing wrangle_openflights_countries.sh ...'
./wrangle_openflights_countries.sh $skip_download_flag

echo 'executing wrangle_openflights_planes.sh ...'
./wrangle_openflights_planes.sh $skip_download_flag

echo 'executing wrangle_openflights_routes.sh ...'
./wrangle_openflights_routes.sh $skip_download_flag


echo 'done'