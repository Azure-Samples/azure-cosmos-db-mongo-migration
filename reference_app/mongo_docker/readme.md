# azure-m2c-wgm-reference-app

## mongodb-docker

Run MongoDB Community Edition Locally as a Docker Container.

## Basic Operations

To run mongodb community edition locally on your macOS/linux laptop,
simply run the following in a Terminal session in the root directory of this repo.  This process should also work on Windows with WSL.

Clone this repo:

```
$ git clone https://github.com/cjoakim/azure-m2c-wgm-reference-app.git
$ cd mongo_docker/
```

Start the MongoDB Community Edition Docker container:

```
$ ./compose.sh up
```

To check the status of the running container:

```
$ ./compose.sh ps
```

To shutdown mongodb and stop the container:

```
$ ./compose.sh down
```

To open a mongo shell to the running database:

```
$ ./mongo_cli.sh local
```

---

## Create and Load the Sample Databases

This section assumes that the local MongoDB is running as a Docker container as described above.

### Openflights Database

This database contains **five collections** of curated data downloaded
from openflights.org.

```
$ ./mongo_recreate_openflights_db.sh
```

#### Query the Data

```
$ ./mongo_cli.sh local
connecting to localhost:27017
MongoDB shell version v4.4.5
...

> show dbs
admin        0.000GB
config       0.000GB
local        0.000GB
olympics     0.032GB
openflights  0.004GB
>
> use openflights
switched to db openflights
>
> show collections
airlines
airports
countries
planes
routes
>
> db.airports.findOne()
{
	"_id" : ObjectId("60b64ff0f815a19b66a07ace"),
	"airport_id" : "2",
	"name" : "Madang Airport",
	"city" : "Madang",
	"country" : "Papua New Guinea",
	"iata_code" : "MAG",
	"icao_code" : "AYMD",
	"latitude" : "-5.20707988739",
	"longitude" : "145.789001465",
	"altitude" : "20",
	"timezone_num" : "10",
	"dst" : "U",
	"timezone_code" : "Pacific/Port_Moresby",
	"type" : "airport",
	"source" : "OurAirports"
}
```

---

### Olympics Database

This database contains **53 collections** of curated data downloaded
from https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

```
$ ./mongo_recreate_openflights_db.sh
```


#### Query the Data

```
$ ./mongo_cli.sh local
connecting to localhost:27017
MongoDB shell version v4.4.5
...

> show dbs
admin        0.000GB
config       0.000GB
local        0.000GB
olympics     0.032GB
openflights  0.004GB
>
> use olympics
>
> use olympics
switched to db olympics
>
> show collections
countries
g1896_summer
g1900_summer
g1904_summer
g1906_summer
g1908_summer
g1912_summer
g1920_summer
g1924_summer
g1924_winter
g1928_summer
g1928_winter
g1932_summer
g1932_winter
g1936_summer
g1936_winter
g1948_summer
g1948_winter
g1952_summer
g1952_winter
g1956_summer
g1956_winter
g1960_summer
g1960_winter
g1964_summer
g1964_winter
g1968_summer
g1968_winter
g1972_summer
g1972_winter
g1976_summer
g1976_winter
g1980_summer
g1980_winter
g1984_summer
g1984_winter
g1988_summer
g1988_winter
g1992_summer
g1992_winter
g1994_winter
g1996_summer
g1998_winter
g2000_summer
g2002_winter
g2004_summer
g2006_winter
g2008_summer
g2010_winter
g2012_summer
g2014_winter
g2016_summer
games
>
> db.g2016_summer.findOne()
{
	"_id" : ObjectId("60b650fcbc6eaa1b218798b6"),
	"id" : "55",
	"name" : "Antonio Abadia Beci",
	"sex" : "m",
	"age" : "26",
	"height" : "170.0",
	"weight" : "65.0",
	"team" : "spain",
	"noc" : "esp",
	"games" : "2016_summer",
	"year" : "2016",
	"season" : "summer",
	"city" : "rio de janeiro",
	"sport" : "athletics",
	"event" : "athletics mens 5000 metres",
	"medal" : "",
	"medal_value" : "0"
}
```
