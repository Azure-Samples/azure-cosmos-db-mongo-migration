#!/bin/bash

# Bash shell script to wrangle/transform a raw mongoexport file
#
# Database Name: olympics
# Generated on:  2021-10-26 19:28:57 UTC
# Template:      wrangle_all.txt

source ./env.sh

skip_download_flag=""  # set to "--skip-download" to bypass blob downloading


echo 'executing wrangle_olympics_countries.sh ...'
./wrangle_olympics_countries.sh $skip_download_flag

echo 'executing wrangle_olympics_g1896_summer.sh ...'
./wrangle_olympics_g1896_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1900_summer.sh ...'
./wrangle_olympics_g1900_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1904_summer.sh ...'
./wrangle_olympics_g1904_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1906_summer.sh ...'
./wrangle_olympics_g1906_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1908_summer.sh ...'
./wrangle_olympics_g1908_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1912_summer.sh ...'
./wrangle_olympics_g1912_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1920_summer.sh ...'
./wrangle_olympics_g1920_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1924_summer.sh ...'
./wrangle_olympics_g1924_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1924_winter.sh ...'
./wrangle_olympics_g1924_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1928_summer.sh ...'
./wrangle_olympics_g1928_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1928_winter.sh ...'
./wrangle_olympics_g1928_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1932_summer.sh ...'
./wrangle_olympics_g1932_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1932_winter.sh ...'
./wrangle_olympics_g1932_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1936_summer.sh ...'
./wrangle_olympics_g1936_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1936_winter.sh ...'
./wrangle_olympics_g1936_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1948_summer.sh ...'
./wrangle_olympics_g1948_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1948_winter.sh ...'
./wrangle_olympics_g1948_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1952_summer.sh ...'
./wrangle_olympics_g1952_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1952_winter.sh ...'
./wrangle_olympics_g1952_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1956_summer.sh ...'
./wrangle_olympics_g1956_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1956_winter.sh ...'
./wrangle_olympics_g1956_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1960_summer.sh ...'
./wrangle_olympics_g1960_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1960_winter.sh ...'
./wrangle_olympics_g1960_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1964_summer.sh ...'
./wrangle_olympics_g1964_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1964_winter.sh ...'
./wrangle_olympics_g1964_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1968_summer.sh ...'
./wrangle_olympics_g1968_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1968_winter.sh ...'
./wrangle_olympics_g1968_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1972_summer.sh ...'
./wrangle_olympics_g1972_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1972_winter.sh ...'
./wrangle_olympics_g1972_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1976_summer.sh ...'
./wrangle_olympics_g1976_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1976_winter.sh ...'
./wrangle_olympics_g1976_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1980_summer.sh ...'
./wrangle_olympics_g1980_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1980_winter.sh ...'
./wrangle_olympics_g1980_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1984_summer.sh ...'
./wrangle_olympics_g1984_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1984_winter.sh ...'
./wrangle_olympics_g1984_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1988_summer.sh ...'
./wrangle_olympics_g1988_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1988_winter.sh ...'
./wrangle_olympics_g1988_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1992_summer.sh ...'
./wrangle_olympics_g1992_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1992_winter.sh ...'
./wrangle_olympics_g1992_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1994_winter.sh ...'
./wrangle_olympics_g1994_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g1996_summer.sh ...'
./wrangle_olympics_g1996_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g1998_winter.sh ...'
./wrangle_olympics_g1998_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g2000_summer.sh ...'
./wrangle_olympics_g2000_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g2002_winter.sh ...'
./wrangle_olympics_g2002_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g2004_summer.sh ...'
./wrangle_olympics_g2004_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g2006_winter.sh ...'
./wrangle_olympics_g2006_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g2008_summer.sh ...'
./wrangle_olympics_g2008_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g2010_winter.sh ...'
./wrangle_olympics_g2010_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g2012_summer.sh ...'
./wrangle_olympics_g2012_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_g2014_winter.sh ...'
./wrangle_olympics_g2014_winter.sh $skip_download_flag

echo 'executing wrangle_olympics_g2016_summer.sh ...'
./wrangle_olympics_g2016_summer.sh $skip_download_flag

echo 'executing wrangle_olympics_games.sh ...'
./wrangle_olympics_games.sh $skip_download_flag


echo 'done'