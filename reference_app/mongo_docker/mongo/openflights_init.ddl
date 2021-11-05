// MongoDB "DDL" initialize the "openflights" database and its collections.
// Chris Joakim, Microsoft, November 2021

// TODO - add indexes 

use OpenFlights

db.Airports.drop()
db.Airlines.drop()
db.Countries.drop()
db.Planes.drop()
db.Routes.drop()

db.createCollection("Airports")
db.createCollection("Airlines")
db.createCollection("Countries")
db.createCollection("Planes")
db.createCollection("Routes")

db.Airports.count()
db.Airlines.count()
db.Countries.count()
db.Planes.count()
db.Routes.count()

show collections
