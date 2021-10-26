#!/bin/bash

# Download html documentation and csv .dat files from openflights.org.
# Chris Joakim, Microsoft, October 2021

echo 'downloading raw/data.html ...'
curl "https://openflights.org/data.html"  > raw/data.html

echo 'downloading raw/airports.dat ...'
curl "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat" > raw/airports.dat

echo 'downloading raw/airlines.dat ...'
curl "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat" > raw/airlines.dat

echo 'downloading raw/routes.dat ...'
curl "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat" > raw/routes.dat

echo 'downloading raw/planes.dat ...'
curl "https://raw.githubusercontent.com/jpatokal/openflights/master/data/planes.dat" > raw/planes.dat

echo 'downloading raw/countries.dat ...'
curl "https://raw.githubusercontent.com/jpatokal/openflights/master/data/countries.dat" > raw/countries.dat

echo 'downloads complete, now head/tail then wc each file ...'

echo 'data.html'
head -5 raw/data.html
tail -5 raw/data.html

echo 'airports.dat'
head -5 raw/airports.dat
tail -5 raw/airports.dat

echo 'airlines.dat'
head -5 raw/airlines.dat
tail -5 raw/airlines.dat

echo 'routes.dat'
head -5 raw/routes.dat
tail -5 raw/routes.dat

echo 'planes.dat'
head -5 raw/planes.dat
tail -5 raw/planes.dat

echo 'countries.dat'
head -5 raw/countries.dat
tail -5 raw/countries.dat

echo '=== wc each file ...'
wc raw/data.html
wc raw/airports.dat
wc raw/airlines.dat
wc raw/routes.dat
wc raw/planes.dat
wc raw/countries.dat

echo 'done'

echo 'TODO: Manually add the header row to each file'
