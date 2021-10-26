# 00 - Purpose

The purpose of this project is to provide a **high-quality, highly-automated, and repeatable process for migrating MongoDB databases to Azure CosmosDB**.

The focus is on **data migration**, 
and **particularly if the migration isn't a simple copy from point A to point B**.
**For example, if the source and target databases have different schemas, or if the documents need to be transformed.**

The project provides both an architecture, and working implementation, of the process.
The process is flexible to allow customization on a case-by-case basis.

### Migration Strategies Supported

1) mongoexport, wrangling/transformation, Azure Blob Storage, load CosmosDB with Azure Data Factory
1) mongoexport, wrangling/transformation, Azure Blob Storage, load CosmosDB with mongoimport
3) mongoexport, wrangling/transformation, Azure Blob Storage, load CosmosDB with DotNet Client program
4) mongoexport, wrangling/transformation, load CosmosDB with mongoimport
5) mongoexport, wrangling/transformation, load CosmosDB with DotNet Client program
6) mongoexport, no transformation, load CosmosDB with mongoimport
7) mongoexport, no transformation, load CosmosDB with DotNet Client program

### Migration aspects that are Not Addressed by this Project

- Application Code Modification
- CosmosDB/Mongo API Database Design - databases, containers, partition keys, RU settings, etc
- CosmosDB/Mongo API Indexing - this depends on your specific application and query patterns

**The Microsoft team will work with you to address these aspects of each migration.**

In the following pages, pages 01 through 16 describe the migration process and its
setup.  Only in step 18 do you actually execute the migration.

The current focus of this project is on migrating MongoDB databases to the 
**CosmosDB/Mongo API**, but the process can easily be modified to target the
**CosmosDB/SQL API**.

## Other Microsoft Solutions to Consider

- https://docs.microsoft.com/en-us/azure/cosmos-db/import-data  (DMT for Cosmos/SQL)
- https://docs.microsoft.com/en-us/azure/dms/tutorial-mongodb-cosmos-db  (DMS)
- https://azure.microsoft.com/en-us/services/database-migration/#features (DMS)
- https://github.com/cjoakim/azure-cosmosdb-adhoc-migrations
