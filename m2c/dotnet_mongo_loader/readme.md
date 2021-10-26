## dotnet_mongo_loader

This directory contains an alternative to Azure Data Factory to load
the target CosmosDB, **using C# code and the net5.0 runtime** with the 
**MongoDB.Driver** SDK.

### Links

- https://www.nuget.org/packages/MongoDB.Driver/
- https://mongodb.github.io/mongo-csharp-driver/2.12/getting_started/quick_tour/
- https://docs.microsoft.com/en-us/dotnet/core/deploying/#publish-framework-dependent

### Build (compile), and Publishing this Console app

```
$ dotnet build
$ dotnet publish

$ dotnet publish
Microsoft (R) Build Engine version 16.9.0+57a23d249 for .NET
Copyright (C) Microsoft Corporation. All rights reserved.

  Determining projects to restore...
  All projects are up-to-date for restore.
  dotnet_mongo_loader -> .../dotnet_mongo_loader/bin/Debug/net5.0/dotnet_mongo_loader.dll
  dotnet_mongo_loader -> .../dotnet_mongo_loader/bin/Debug/net5.0/publish/
```

### Execute the Console App

The dotnet project can be executed like this (from the parent directory):

```
$ dotnet run --project dotnet_mongo_loader/dotnet_mongo_loader.csproj
```

```
if [ $M2C_COSMOS_LOAD_METHOD == "dotnet_mongo_loader" ];
then
    echo ''
    echo 'executing dotnet_mongo_loader to db: olympics coll: games ...' 

    dotnet run --project dotnet_mongo_loader/dotnet_mongo_loader.csproj \
        olympics games tmp/olympics/olympics__g1992_winter__wrangled.json \
        $M2C_DOTNETMONGOLOADER_TARGET $M2C_DOTNETMONGOLOADER_LOAD_IND \
        $M2C_DOTNETMONGOLOADER_DOCUMENT_ID_POLICY \
        --tracerInterval $M2C_DOTNETMONGOLOADER_TRACER_INTERVAL \
        --rowMaxRetries $M2C_DOTNETMONGOLOADER_ROW_MAX_RETRIES \
        $M2C_DOTNETMONGOLOADER_VERBOSE
fi
```

## Results - dotnet_mongo_loader

```
executing dotnet_mongo_loader to db: travel coll: routes ...
args length: 11
arg: travel
arg: routes
arg: tmp/openflights/openflights__routes__wrangled.json
arg: --targetCosmos
arg: --load
arg: --createNewDocIds
arg: --tracerInterval
arg: 1000
arg: --rowMaxRetries
arg: 10
arg: --quiet
Args used this run:
  dbname:          travel
  collname:        routes
  infile:          tmp/openflights/openflights__routes__wrangled.json
  target:          cosmos
  verbose:         False
  createNewDocIds: True
  tracerInterval:  1000
  rowMaxRetries:   10
MongoClient created for target: cosmos
ProcessingLoop - start, line: 0, minutes: 0, retries: 0, failures: 0
ProcessingLoop - interval, line: 1000, minutes: 0.133, retries: 0, failures: 0
ProcessingLoop - interval, line: 2000, minutes: 0.2535, retries: 0, failures: 0
ProcessingLoop - interval, line: 3000, minutes: 0.3733666666666667, retries: 0, failures: 0
ProcessingLoop - interval, line: 4000, minutes: 0.4888166666666667, retries: 0, failures: 0
ProcessingLoop - interval, line: 5000, minutes: 0.6062, retries: 0, failures: 0
ProcessingLoop - interval, line: 6000, minutes: 0.723, retries: 0, failures: 0
ProcessingLoop - interval, line: 7000, minutes: 0.83975, retries: 0, failures: 0
ProcessingLoop - interval, line: 8000, minutes: 0.95655, retries: 0, failures: 0
ProcessingLoop - interval, line: 9000, minutes: 1.0749666666666666, retries: 0, failures: 0
ProcessingLoop - interval, line: 10000, minutes: 1.1931333333333334, retries: 0, failures: 0
ProcessingLoop - interval, line: 11000, minutes: 1.3108166666666667, retries: 0, failures: 0
ProcessingLoop - interval, line: 12000, minutes: 1.4277, retries: 0, failures: 0
ProcessingLoop - interval, line: 13000, minutes: 1.5429, retries: 0, failures: 0
ProcessingLoop - interval, line: 14000, minutes: 1.658, retries: 0, failures: 0
ProcessingLoop - interval, line: 15000, minutes: 1.7753166666666667, retries: 0, failures: 0
ProcessingLoop - interval, line: 16000, minutes: 1.891, retries: 0, failures: 0
ProcessingLoop - interval, line: 17000, minutes: 2.0101333333333335, retries: 0, failures: 0
ProcessingLoop - interval, line: 18000, minutes: 2.1279, retries: 0, failures: 0
ProcessingLoop - interval, line: 19000, minutes: 2.24855, retries: 0, failures: 0
ProcessingLoop - interval, line: 20000, minutes: 2.3679333333333332, retries: 0, failures: 0
ProcessingLoop - interval, line: 21000, minutes: 2.48775, retries: 0, failures: 0
ProcessingLoop - interval, line: 22000, minutes: 2.6078333333333332, retries: 0, failures: 0
ProcessingLoop - interval, line: 23000, minutes: 2.726, retries: 0, failures: 0
ProcessingLoop - interval, line: 24000, minutes: 2.8397166666666664, retries: 0, failures: 0
ProcessingLoop - interval, line: 25000, minutes: 2.95675, retries: 0, failures: 0
ProcessingLoop - interval, line: 26000, minutes: 3.07525, retries: 0, failures: 0
ProcessingLoop - interval, line: 27000, minutes: 3.19455, retries: 0, failures: 0
ProcessingLoop - interval, line: 28000, minutes: 3.3134333333333332, retries: 0, failures: 0
ProcessingLoop - interval, line: 29000, minutes: 3.431433333333333, retries: 0, failures: 0
ProcessingLoop - interval, line: 30000, minutes: 3.5473333333333334, retries: 0, failures: 0
ProcessingLoop - interval, line: 31000, minutes: 3.6632666666666664, retries: 0, failures: 0
ProcessingLoop - interval, line: 32000, minutes: 3.78085, retries: 0, failures: 0
ProcessingLoop - interval, line: 33000, minutes: 3.898833333333333, retries: 0, failures: 0
ProcessingLoop - interval, line: 34000, minutes: 4.019, retries: 0, failures: 0
ProcessingLoop - interval, line: 35000, minutes: 4.138483333333333, retries: 0, failures: 0
ProcessingLoop - interval, line: 36000, minutes: 4.2575666666666665, retries: 0, failures: 0
ProcessingLoop - interval, line: 37000, minutes: 4.375233333333333, retries: 0, failures: 0
ProcessingLoop - interval, line: 38000, minutes: 4.490566666666667, retries: 0, failures: 0
ProcessingLoop - interval, line: 39000, minutes: 4.60365, retries: 0, failures: 0
ProcessingLoop - interval, line: 40000, minutes: 4.71795, retries: 0, failures: 0
ProcessingLoop - interval, line: 41000, minutes: 4.8327, retries: 0, failures: 0
ProcessingLoop - interval, line: 42000, minutes: 4.950233333333333, retries: 0, failures: 0
ProcessingLoop - interval, line: 43000, minutes: 5.0682833333333335, retries: 0, failures: 0
ProcessingLoop - interval, line: 44000, minutes: 5.1871, retries: 0, failures: 0
ProcessingLoop - interval, line: 45000, minutes: 5.306333333333333, retries: 0, failures: 0
ProcessingLoop - interval, line: 46000, minutes: 5.427233333333334, retries: 0, failures: 0
ProcessingLoop - interval, line: 47000, minutes: 5.5449166666666665, retries: 0, failures: 0
ProcessingLoop - interval, line: 48000, minutes: 5.661533333333334, retries: 0, failures: 0
ProcessingLoop - interval, line: 49000, minutes: 5.77885, retries: 0, failures: 0
ProcessingLoop - interval, line: 50000, minutes: 5.89405, retries: 0, failures: 0
ProcessingLoop - interval, line: 51000, minutes: 6.0126, retries: 0, failures: 0
ProcessingLoop - interval, line: 52000, minutes: 6.131366666666667, retries: 0, failures: 0
ProcessingLoop - interval, line: 53000, minutes: 6.2523, retries: 0, failures: 0
ProcessingLoop - interval, line: 54000, minutes: 6.372733333333334, retries: 0, failures: 0
ProcessingLoop - interval, line: 55000, minutes: 6.4893833333333335, retries: 0, failures: 0
ProcessingLoop - interval, line: 56000, minutes: 6.605883333333334, retries: 0, failures: 0
ProcessingLoop - interval, line: 57000, minutes: 6.720716666666666, retries: 0, failures: 0
ProcessingLoop - interval, line: 58000, minutes: 6.837383333333333, retries: 0, failures: 0
ProcessingLoop - interval, line: 59000, minutes: 6.953783333333333, retries: 0, failures: 0
ProcessingLoop - interval, line: 60000, minutes: 7.073433333333333, retries: 0, failures: 0
ProcessingLoop - interval, line: 61000, minutes: 7.192966666666667, retries: 0, failures: 0
ProcessingLoop - interval, line: 62000, minutes: 7.312866666666666, retries: 0, failures: 0
ProcessingLoop - interval, line: 63000, minutes: 7.432333333333333, retries: 0, failures: 0
ProcessingLoop - interval, line: 64000, minutes: 7.550333333333334, retries: 0, failures: 0
ProcessingLoop - interval, line: 65000, minutes: 7.669316666666667, retries: 0, failures: 0
ProcessingLoop - interval, line: 66000, minutes: 7.789483333333333, retries: 0, failures: 0
ProcessingLoop - interval, line: 67000, minutes: 7.9103, retries: 0, failures: 0
ProcessingLoop - completed, line: 67663, minutes: 7.989466666666667, retries: 0, failures: 0
done
```

## Results - mongoimport

```

```