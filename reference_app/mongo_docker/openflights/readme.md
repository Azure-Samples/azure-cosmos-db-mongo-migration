# Openflights Data

The downloaded *.dat files contain no header rows.  
Add these manually, per their documented fields.

```
airlines.dat
airline_id,name,alias,iata,icao,callsign,country,active

airports.dat
airport_id,name,city,country,iata_code,icao_code,latitude,longitude,altitude,timezone_num,dst,timezone_code,type,source

countries.dat
name,iso_code,dafif_code

planes.dat
name,iata,icao

routes.dat
airline_id,openflights_airline_id,from_airport,openflights_from_airport,to_airport,openflights_to_airport,x,codeshare,equipment
```
