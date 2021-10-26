# azure-cosmos-db-mongo-migration

<p align="center"><img src="docs/img/architecture.png" width="99%"></p>

## Features

This project framework provides the following features:

- **MongoDB to CosmosDB Data Migration**
- **Seven migration approaches are supported** by this project
  1) mongoexport, wrangling/transformation, Azure Blob Storage, load CosmosDB with Azure Data Factory
  1) mongoexport, wrangling/transformation, Azure Blob Storage, load CosmosDB with mongoimport
  1) mongoexport, wrangling/transformation, Azure Blob Storage, load CosmosDB with DotNet Client program
  1) mongoexport, wrangling/transformation, load CosmosDB with mongoimport
  1) mongoexport, wrangling/transformation, load CosmosDB with DotNet Client program
  1) mongoexport, no transformation, load CosmosDB with mongoimport
  1) mongoexport, no transformation, load CosmosDB with DotNet Client program

- **The Process uses metadata-driven code generation to generate artifacts**
  - shell scripts
  - configuration files
  - Azure Data Factory JSON code files
- A **User-edited mapping file which maps source to target databases**, can be generated
- The **intent is to have zero human edits of the generated code/artifacts**
- The **mongoexport** utility is used to extract data from the source database/containers
- The Process supports optionally transforming your collection/container design
- The Process supports data transformation from source to target database

## Getting Started

[See the Documentation](docs/README.md) and clone this repository.

### Prerequisites

- git
- python 3
- mongo tooling - mongoexport, mongoimport, mongo shell
- Developer workstation of any OS (macOS, Windows, Linux)
- Azure CLI program, az
- Ubuntu Virtual Machine(s) in Azure to execute the majority of the process
- Docker for executing the Reference Application locally
- Your source-control system that is network-accessable to Azure VMs
- [See the docs on workstation setup](docs/03_development_computer_setup.md)

### Installation

Clone this GitHub repository to your Development workstation and/or VM
with network access to your current MongoDB database(s).

```
$ git clone https://github.com/Azure-Samples/azure-cosmos-db-mongo-migration.git
```

**Then copy this project to your Git or other source-control system.**

It is assumed that your source-control system (GitHub, Azure DevOps, etc)
has network access to Azure VMs.

### Quickstart

[See the Documentation](docs/README.md)

## Demo

A [Reference Application](reference_app/readme.md) is included in this repository
to show how to use this migration process.

This reference application database can be deployed to either a Docker-containerized
MongoDB instance, or to your development MongoDB instance.

See [running MongoDB locally as a Docker container](reference_app/mongo_docker/readme.md).

## Resources

- [Azure Cosmos DB](https://azure.microsoft.com/en-us/services/cosmos-db/)
- [Azure Cosmos DB API for MongoDB](https://docs.microsoft.com/en-us/azure/cosmos-db/mongodb/mongodb-introduction)
- [mongoexport](https://docs.mongodb.com/database-tools/mongoexport/)
- [Azure Data Factory](https://docs.microsoft.com/en-us/azure/data-factory/)
