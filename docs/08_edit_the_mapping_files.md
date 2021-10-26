# 08 - Edit the Mapping Files

## Wait, what about the design of the target CosmosDB database?

**This is the time to think very carefully about the design of your CosmosDB database**.

Often the design will not be equivalent to the source MongoDB design regarding
the number of collections/containers, partition/shard keys, document types, document size,
and indexing.

Some items to consider:

- **Partition Keys:** Choosing an appropriate partition key is critical to both the 
costs and performance of your CosmosDB database.  Strive to utilize the Partition Key (i.e. - pk)
in most of your queries.

- **Shared Throughput:** Strive to migrate a MongoDB database with many collections to a CosmosDB
database with **25 or fewer collections**, so as to take advantage of shared throughput at the 
CosmosDB database level.

- **Indexing:** Indexing in CosmosDB is just as important as in MongoDB.  Index the attributes
that you query on.

- **Document Types:** In cases where you consolidate many MongoDB collections into one CosmosDB
container, or in cases where you store dissimilar documents in the same container, you can
utilize a document-type attribute, offen named **doctype**.  The built-in wrangling/transformation
logic in this migration process supports this functionality.

- **Document Size:** Prefer to use smaller documents, give related documents the same partition
key value so that they can be read efficiently.  Be aware of large or unbounded arrays within
your documents and extract this data to other documents.

### Links

- https://docs.microsoft.com/en-us/azure/cosmos-db/modeling-data
- https://docs.microsoft.com/en-us/azure/cosmos-db/mongodb-introduction
- https://docs.microsoft.com/en-us/azure/cosmos-db/set-throughput#set-throughput-on-a-database

After addressing these design issues, please proceed to the editing and/or generating
your mapping files.

---

## The Mapping Files 

Please see documentation page [07 - Generate Mapping Files](07_generate_mapping_files.md)
regarding the mapping file format and generation.

It is recommended that you generate these files with code rather than edit them
by hand, as they are verbose JSON files.

However, if you feed the need to edit these files, please see the previous page
regarding the format and content of these files.

Examples are here:

```
reference_app/data/metadata/olympics_mapping.json
reference_app/data/metadata/openflights_mapping.json
```

Once these mapping files are **finalized, or completed** please proceed to the
next pages, which uses the mapping files for **artifact generation**.

**This step is typically executed from a Developer laptop.**

### Alternative Wrangling/Transformation

This migration process implements an **"opinionated"** design regarding the
wrangling or transformation of the mongoexport files from "raw" format
to "adf-ready" format.

Each customer may certainly implement alternative ways to transform the
mongoexport files.  If you choose to use Python, please look at file 
**standard_doc_wrangler.py** in this repository and consider a similar
implementation.
