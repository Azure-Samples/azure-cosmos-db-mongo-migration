// MongoDB "DDL" initialize the "openflights" database and its collections.
// Chris Joakim, Microsoft, October 2021

// TODO - add indexes 

use openflights

db.airports.drop()
db.airlines.drop()
db.countries.drop()
db.planes.drop()
db.routes.drop()

db.createCollection("airports")
db.createCollection("airlines")
db.createCollection("countries")
db.createCollection("planes")
db.createCollection("routes")

db.airports.count()
db.airlines.count()
db.countries.count()
db.planes.count()
db.routes.count()

show collections
