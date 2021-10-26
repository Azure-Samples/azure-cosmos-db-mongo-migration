// MongoDB "DDL" initialize the "olympics" database and its collections.
// Chris Joakim, Microsoft, October 2021

// TODO - add additional indexes if necessary

use olympics

db.games.drop()
db.countries.drop()
db.g1896_summer.drop()
db.g1900_summer.drop()
db.g1904_summer.drop()
db.g1906_summer.drop()
db.g1908_summer.drop()
db.g1912_summer.drop()
db.g1920_summer.drop()
db.g1924_summer.drop()
db.g1924_winter.drop()
db.g1928_summer.drop()
db.g1928_winter.drop()
db.g1932_summer.drop()
db.g1932_winter.drop()
db.g1936_summer.drop()
db.g1936_winter.drop()
db.g1948_summer.drop()
db.g1948_winter.drop()
db.g1952_summer.drop()
db.g1952_winter.drop()
db.g1956_summer.drop()
db.g1956_winter.drop()
db.g1960_summer.drop()
db.g1960_winter.drop()
db.g1964_summer.drop()
db.g1964_winter.drop()
db.g1968_summer.drop()
db.g1968_winter.drop()
db.g1972_summer.drop()
db.g1972_winter.drop()
db.g1976_summer.drop()
db.g1976_winter.drop()
db.g1980_summer.drop()
db.g1980_winter.drop()
db.g1984_summer.drop()
db.g1984_winter.drop()
db.g1988_summer.drop()
db.g1988_winter.drop()
db.g1992_summer.drop()
db.g1992_winter.drop()
db.g1994_winter.drop()
db.g1996_summer.drop()
db.g1998_winter.drop()
db.g2000_summer.drop()
db.g2002_winter.drop()
db.g2004_summer.drop()
db.g2006_winter.drop()
db.g2008_summer.drop()
db.g2010_winter.drop()
db.g2012_summer.drop()
db.g2014_winter.drop()
db.g2016_summer.drop()

db.createCollection("games")
db.createCollection("countries")
db.createCollection("g1896_summer")
db.createCollection("g1900_summer")
db.createCollection("g1904_summer")
db.createCollection("g1906_summer")
db.createCollection("g1908_summer")
db.createCollection("g1912_summer")
db.createCollection("g1920_summer")
db.createCollection("g1924_summer")
db.createCollection("g1924_winter")
db.createCollection("g1928_summer")
db.createCollection("g1928_winter")
db.createCollection("g1932_summer")
db.createCollection("g1932_winter")
db.createCollection("g1936_summer")
db.createCollection("g1936_winter")
db.createCollection("g1948_summer")
db.createCollection("g1948_winter")
db.createCollection("g1952_summer")
db.createCollection("g1952_winter")
db.createCollection("g1956_summer")
db.createCollection("g1956_winter")
db.createCollection("g1960_summer")
db.createCollection("g1960_winter")
db.createCollection("g1964_summer")
db.createCollection("g1964_winter")
db.createCollection("g1968_summer")
db.createCollection("g1968_winter")
db.createCollection("g1972_summer")
db.createCollection("g1972_winter")
db.createCollection("g1976_summer")
db.createCollection("g1976_winter")
db.createCollection("g1980_summer")
db.createCollection("g1980_winter")
db.createCollection("g1984_summer")
db.createCollection("g1984_winter")
db.createCollection("g1988_summer")
db.createCollection("g1988_winter")
db.createCollection("g1992_summer")
db.createCollection("g1992_winter")
db.createCollection("g1994_winter")
db.createCollection("g1996_summer")
db.createCollection("g1998_winter")
db.createCollection("g2000_summer")
db.createCollection("g2002_winter")
db.createCollection("g2004_summer")
db.createCollection("g2006_winter")
db.createCollection("g2008_summer")
db.createCollection("g2010_winter")
db.createCollection("g2012_summer")
db.createCollection("g2014_winter")
db.createCollection("g2016_summer")

db.games.count()
db.countries.count()
db.g1896_summer.count()
db.g1900_summer.count()
db.g1904_summer.count()
db.g1906_summer.count()
db.g1908_summer.count()
db.g1912_summer.count()
db.g1920_summer.count()
db.g1924_summer.count()
db.g1924_winter.count()
db.g1928_summer.count()
db.g1928_winter.count()
db.g1932_summer.count()
db.g1932_winter.count()
db.g1936_summer.count()
db.g1936_winter.count()
db.g1948_summer.count()
db.g1948_winter.count()
db.g1952_summer.count()
db.g1952_winter.count()
db.g1956_summer.count()
db.g1956_winter.count()
db.g1960_summer.count()
db.g1960_winter.count()
db.g1964_summer.count()
db.g1964_winter.count()
db.g1968_summer.count()
db.g1968_winter.count()
db.g1972_summer.count()
db.g1972_winter.count()
db.g1976_summer.count()
db.g1976_winter.count()
db.g1980_summer.count()
db.g1980_winter.count()
db.g1984_summer.count()
db.g1984_winter.count()
db.g1988_summer.count()
db.g1988_winter.count()
db.g1992_summer.count()
db.g1992_winter.count()
db.g1994_winter.count()
db.g1996_summer.count()
db.g1998_winter.count()
db.g2000_summer.count()
db.g2002_winter.count()
db.g2004_summer.count()
db.g2006_winter.count()
db.g2008_summer.count()
db.g2010_winter.count()
db.g2012_summer.count()
db.g2014_winter.count()
db.g2016_summer.count()

show collections
