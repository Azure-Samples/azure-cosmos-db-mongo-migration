#!/bin/bash

# Bash and python script to wrangle the raw data files in the olympics/raw/
# directory into mongoimport files in the olympics/import_json/ directory.
# Users of this repo don't need to execute this script, as the output files
# are already present in the olympics/import_json/ directory.
# Chris Joakim, Microsoft, October 2021

mkdir -p tmp

echo 'parse_raw_athlete_events_to_csv ...'
python main.py parse_raw_athlete_events_to_csv

echo 'identify_unique_games_to_json ...'
python main.py identify_unique_games_to_json    > ../olympics/import_json/games.json

echo 'parse_countries_csv_to_json ...'
python main.py parse_countries_csv_to_json      > ../olympics/import_json/countries.json

# See code generation in main.py generate_games_script_commands()

echo 'parsing game 1896_summer'
python main.py parse_athlete_events_csv_to_json 1896_summer > ../olympics/import_json/g1896_summer.json

echo 'parsing game 1900_summer'
python main.py parse_athlete_events_csv_to_json 1900_summer > ../olympics/import_json/g1900_summer.json

echo 'parsing game 1904_summer'
python main.py parse_athlete_events_csv_to_json 1904_summer > ../olympics/import_json/g1904_summer.json

echo 'parsing game 1906_summer'
python main.py parse_athlete_events_csv_to_json 1906_summer > ../olympics/import_json/g1906_summer.json

echo 'parsing game 1908_summer'
python main.py parse_athlete_events_csv_to_json 1908_summer > ../olympics/import_json/g1908_summer.json

echo 'parsing game 1912_summer'
python main.py parse_athlete_events_csv_to_json 1912_summer > ../olympics/import_json/g1912_summer.json

echo 'parsing game 1920_summer'
python main.py parse_athlete_events_csv_to_json 1920_summer > ../olympics/import_json/g1920_summer.json

echo 'parsing game 1924_summer'
python main.py parse_athlete_events_csv_to_json 1924_summer > ../olympics/import_json/g1924_summer.json

echo 'parsing game 1924_winter'
python main.py parse_athlete_events_csv_to_json 1924_winter > ../olympics/import_json/g1924_winter.json

echo 'parsing game 1928_summer'
python main.py parse_athlete_events_csv_to_json 1928_summer > ../olympics/import_json/g1928_summer.json

echo 'parsing game 1928_winter'
python main.py parse_athlete_events_csv_to_json 1928_winter > ../olympics/import_json/g1928_winter.json

echo 'parsing game 1932_summer'
python main.py parse_athlete_events_csv_to_json 1932_summer > ../olympics/import_json/g1932_summer.json

echo 'parsing game 1932_winter'
python main.py parse_athlete_events_csv_to_json 1932_winter > ../olympics/import_json/g1932_winter.json

echo 'parsing game 1936_summer'
python main.py parse_athlete_events_csv_to_json 1936_summer > ../olympics/import_json/g1936_summer.json

echo 'parsing game 1936_winter'
python main.py parse_athlete_events_csv_to_json 1936_winter > ../olympics/import_json/g1936_winter.json

echo 'parsing game 1948_summer'
python main.py parse_athlete_events_csv_to_json 1948_summer > ../olympics/import_json/g1948_summer.json

echo 'parsing game 1948_winter'
python main.py parse_athlete_events_csv_to_json 1948_winter > ../olympics/import_json/g1948_winter.json

echo 'parsing game 1952_summer'
python main.py parse_athlete_events_csv_to_json 1952_summer > ../olympics/import_json/g1952_summer.json

echo 'parsing game 1952_winter'
python main.py parse_athlete_events_csv_to_json 1952_winter > ../olympics/import_json/g1952_winter.json

echo 'parsing game 1956_summer'
python main.py parse_athlete_events_csv_to_json 1956_summer > ../olympics/import_json/g1956_summer.json

echo 'parsing game 1956_winter'
python main.py parse_athlete_events_csv_to_json 1956_winter > ../olympics/import_json/g1956_winter.json

echo 'parsing game 1960_summer'
python main.py parse_athlete_events_csv_to_json 1960_summer > ../olympics/import_json/g1960_summer.json

echo 'parsing game 1960_winter'
python main.py parse_athlete_events_csv_to_json 1960_winter > ../olympics/import_json/g1960_winter.json

echo 'parsing game 1964_summer'
python main.py parse_athlete_events_csv_to_json 1964_summer > ../olympics/import_json/g1964_summer.json

echo 'parsing game 1964_winter'
python main.py parse_athlete_events_csv_to_json 1964_winter > ../olympics/import_json/g1964_winter.json

echo 'parsing game 1968_summer'
python main.py parse_athlete_events_csv_to_json 1968_summer > ../olympics/import_json/g1968_summer.json

echo 'parsing game 1968_winter'
python main.py parse_athlete_events_csv_to_json 1968_winter > ../olympics/import_json/g1968_winter.json

echo 'parsing game 1972_summer'
python main.py parse_athlete_events_csv_to_json 1972_summer > ../olympics/import_json/g1972_summer.json

echo 'parsing game 1972_winter'
python main.py parse_athlete_events_csv_to_json 1972_winter > ../olympics/import_json/g1972_winter.json

echo 'parsing game 1976_summer'
python main.py parse_athlete_events_csv_to_json 1976_summer > ../olympics/import_json/g1976_summer.json

echo 'parsing game 1976_winter'
python main.py parse_athlete_events_csv_to_json 1976_winter > ../olympics/import_json/g1976_winter.json

echo 'parsing game 1980_summer'
python main.py parse_athlete_events_csv_to_json 1980_summer > ../olympics/import_json/g1980_summer.json

echo 'parsing game 1980_winter'
python main.py parse_athlete_events_csv_to_json 1980_winter > ../olympics/import_json/g1980_winter.json

echo 'parsing game 1984_summer'
python main.py parse_athlete_events_csv_to_json 1984_summer > ../olympics/import_json/g1984_summer.json

echo 'parsing game 1984_winter'
python main.py parse_athlete_events_csv_to_json 1984_winter > ../olympics/import_json/g1984_winter.json

echo 'parsing game 1988_summer'
python main.py parse_athlete_events_csv_to_json 1988_summer > ../olympics/import_json/g1988_summer.json

echo 'parsing game 1988_winter'
python main.py parse_athlete_events_csv_to_json 1988_winter > ../olympics/import_json/g1988_winter.json

echo 'parsing game 1992_summer'
python main.py parse_athlete_events_csv_to_json 1992_summer > ../olympics/import_json/g1992_summer.json

echo 'parsing game 1992_winter'
python main.py parse_athlete_events_csv_to_json 1992_winter > ../olympics/import_json/g1992_winter.json

echo 'parsing game 1994_winter'
python main.py parse_athlete_events_csv_to_json 1994_winter > ../olympics/import_json/g1994_winter.json

echo 'parsing game 1996_summer'
python main.py parse_athlete_events_csv_to_json 1996_summer > ../olympics/import_json/g1996_summer.json

echo 'parsing game 1998_winter'
python main.py parse_athlete_events_csv_to_json 1998_winter > ../olympics/import_json/g1998_winter.json

echo 'parsing game 2000_summer'
python main.py parse_athlete_events_csv_to_json 2000_summer > ../olympics/import_json/g2000_summer.json

echo 'parsing game 2002_winter'
python main.py parse_athlete_events_csv_to_json 2002_winter > ../olympics/import_json/g2002_winter.json

echo 'parsing game 2004_summer'
python main.py parse_athlete_events_csv_to_json 2004_summer > ../olympics/import_json/g2004_summer.json

echo 'parsing game 2006_winter'
python main.py parse_athlete_events_csv_to_json 2006_winter > ../olympics/import_json/g2006_winter.json

echo 'parsing game 2008_summer'
python main.py parse_athlete_events_csv_to_json 2008_summer > ../olympics/import_json/g2008_summer.json

echo 'parsing game 2010_winter'
python main.py parse_athlete_events_csv_to_json 2010_winter > ../olympics/import_json/g2010_winter.json

echo 'parsing game 2012_summer'
python main.py parse_athlete_events_csv_to_json 2012_summer > ../olympics/import_json/g2012_summer.json

echo 'parsing game 2014_winter'
python main.py parse_athlete_events_csv_to_json 2014_winter > ../olympics/import_json/g2014_winter.json

echo 'parsing game 2016_summer'
python main.py parse_athlete_events_csv_to_json 2016_summer > ../olympics/import_json/g2016_summer.json

#

echo 'generate_games_import_commands ...'
python main.py generate_games_import_commands   > tmp/games_import_commands.txt

echo 'generate_mongo_init_commands ...'
python main.py generate_mongo_init_commands     > tmp/mongo_init_commands.txt

echo 'done'
