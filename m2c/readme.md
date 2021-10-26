# Mongo-to-Cosmos Migration

## Reference Database

This repo contains a set of **olympics** history data that can
be loaded to a Mongo Database for the purpose of working through
this migration process.  See the **sample_db/** directory.

## Steps in the Process

### Initialize

- Capture Source Database Metadata to JSON file(s)
- Manually Edit/Append the Metadata files
  - Specify data-wrangling location: local/files or Azure Container Instances/Blobs
  - Specify source-database to target-database collection mapping
  - Specify partition-key logic for each target collection
    - partition_key attribute name
    - partition_key attribute value population logic
  - Specify Azure Blob Storage location

### Generate

- Generate mongoexport scripts vs source database
- Generate mongoexport Blob Upload scripts (optional)
- Generate Wrangling scripts; local or ACI (powershell or bash)
- Generate Azure Data Factory Dataset JSON files
- Generate Azure Data Factory Pipeline JSON file(s)

### Execute Data Wrangling

- Wrangle input mongoexport files to mongoexport files/blobs for ADF

### Execute Database Load

- Use Azure Data Factory (ADF) Pipeline(s) to Copy to target CosmosDB

---



## Misc

```
db.runCommand({getLastRequestStatistics: 1})
```