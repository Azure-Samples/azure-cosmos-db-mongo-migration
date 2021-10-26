# 02 - Reference Application

A companion **Reference Application** has been created for two reasons:

- For Azure/Cosmos customers to understand this migration process
- For Development and Testing of this process itself

This reference application in this sibling GitHub repository:
https://github.com/cjoakim/azure-m2c-wgm-reference-app 

The separate sibling repo was created so as not to clutter this primary
implementation repository with extraneous content.

**It is strongly recommended that you do a practice migration with the reference application before migrating your actual databases.**

## Reference Databases

Mongoexport files for two separate curated databases have been created:

- **olympics** - 53 collections.  Summer and Winter games from 1896 to 2016, etc.
- **openflights** - 5 collections.  Countries, airports, airplanes, etc.

The olympics database was specifically created to demonstrate **consolidating**
a MongoDB database with many collections into a CosmosDB database with much
fewer collections so as to take advantage of **CosmosDB Database Shared Throughput**.
Likewise, the olympics database demonstrates the necessary mappings and data wrangling
before the data can be loaded into CosmosDB.

See https://docs.microsoft.com/en-us/azure/cosmos-db/set-throughput#set-throughput-on-a-database

See the **mongo_docker/** directory of the sibling repository for these reference databases.
This directory also provides scripts to load this data into a MongoDB Community Edition
database as a **Docker Container**.

## Reference Artifacts

See the **reference_app/** directory of the sibling reposity for a complete
set of generated artifacts for the olympics and openflights databases.

The intent of these is twofold:

- Provide examples for visual browing and understanding
- They are executable as-is, for testing the migration process

**Please look at the reference_app/ directory to understand what artifacts are generated by this process.**

## Sibling Repository Directory Structure

The following tree should help you understand the structure and contents of the
sibling reference implementation GitHub repository.

```
├── mongo_docker
│   ├── mongo
│   ├── olympics
│   │   ├── import_json
│   │   └── raw
│   └── openflights
│       ├── import_json
│       └── raw
└── reference_app
    ├── artifacts
    │   ├── adf
    │   │   ├── dataset
    │   │   ├── linkedService
    │   │   └── pipeline
    │   └── shell
    │       ├── mongo
    │       ├── pysrc
    │       └── tmp
    │           ├── olympics
    │           └── openflights
    └── data
        ├── metadata
        └── mongoexports
            ├── olympics
            └── openflights
```