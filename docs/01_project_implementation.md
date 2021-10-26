# 01 - Project Implementation

The project adopts a unix philosophy of building a complex system from a series
of simple programs.

In **unix/linux pseudocode**, the processing pipeline looks like this:

```
extract_metadata | generate_artifacts | mongoexport | blob_upload | wrangle_transform | load_cosmosdb_with_adf
```

## MongoDB

The **Source Database** is assumed to be MongoDB.  This can be located either on-prem,
or in another cloud hosting environment.

## mongoexport 

The [mongoexport utility program](https://docs.mongodb.com/manual/reference/program/mongoexport/)
is used heavily by this project.

This program is used to export data, in a JSON text format, from a MongoDB collection.  The file
format is **one-document-per-line** in the export file.

This is an example row, for Allyson Felix in the 2016 Summer Olympics:
```
{"_id":{"$oid":"60bf6af5490f533a75494ca8"},"id":"34551","name":"Allyson Michelle Felix","sex":"f","age":"30","height":"168.0","weight":"56.0","team":"united states","noc":"usa","games":"2016_summer","year":"2016","season":"summer","city":"rio de janeiro","sport":"athletics","event":"athletics womens 4 x 100 metres relay","medal":"gold","medal_value":"3"}
```

There is a corresponding program called [mongoimport](https://docs.mongodb.com/manual/reference/program/mongoimport/)
that can be used to load a mongoexport file into a target Mongo container.  **Azure CosmosDB with Mongo API**
does support the use of the mongoimport program.  However, this project uses **Azure Data Factory (ADF)** for
importing data into CosmosDB, as it is aware of CosmosDB throughput, implements retry logic, and is thus
more reliable that mongoimport.

## Python3

Python version 3.x (i.e. - 3.8.6) is used for several purposes in this project:
- Source Database Metadata extraction, using the **pymongo** library
- Automated code and file **Artifact Generation** using the **Jinja2** library
- Azure Storage container creation with the **azure-storage-blob** library
- Azure Storage Blob uploading and downloading, also with the **azure-storage-blob** library
- **Data Wrangling** - transforming the raw mongoexport files into a similar format for loading into CosmosDB with ADF.

See https://www.python.org

## Shell Scripts

Many of the generated artifacts are **bash shell scripts**.  These scripts, along with all of the
generated artifacts, are **intended to be used as-is; no editing of these is required**.

The bash shell scripts can be executed on a **linux, macOS, or Windows 10 laptop with WSL**.

However, the generated **wrangling** scripts are intended to be executed on an 
**Ubuntu Linux Virtual Machine in Azure**.

See https://www.gnu.org/software/bash/

## Azure Blob Storage

Azure Storage is used to hold both the **raw mongoexport** files (i.e. - blobs) as well
as the **wrangled mongoexport** files for ADF.

See https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction

## Azure Data Factory, ADF

Azure Data Factory is used to copy the wrangled mongoexport blobs into the appropriate
target CosmosDB container.

The project generates ADF Linked Services, Datasets, and Pipelines.
These are used verbatim, with no editing required after generation.

The ADF artifacts can be added to a **git repository**, and imported into ADF via git.

See https://azure.microsoft.com/en-us/services/data-factory/

## Azure CosmosDB

**Azure CosmosDB** is the **Target Database** 

See https://docs.microsoft.com/en-us/azure/cosmos-db/mongodb-introduction 
