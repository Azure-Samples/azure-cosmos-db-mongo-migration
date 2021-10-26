# 03 - Development Computer Setup

A Developer laptop can be used to execute much of the migration process, including:

- Source Database Metadata Extraction
- Artifact Generation
- Azure Data Factory - use in Azure Portal, and ADF Pipeline execution

However, a **Azure VMs** are recommended for most of the actual migration execution;
see [18 - Execute Migration](18_execute_migration.md).

## Software Requirements

The following software is required on your **"Development Workstation"**
as well as on the Azure Virtual Machines used for your migrations.
Your "Development Workstation" could be a laptop, a server, or a VM.

- **git** source control program.  See https://git-scm.com 
- **bash** shell.  Available on Linux, macOS, or Windows 10 with WSL.
- **python3**.  See https://www.python.org.  The project was developed and tested with python 3.8.6.
- **mongo client** - from MongoDB Community Edition
- **Azure CLI (az)** - See https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
  - The az CLI is used in this project to:
    - Upload files to Azure Blob Storage
    - Submit Azure Data Factory pipelines
    - Optionally provision Azure Resources, such as Storage, ADF, and CosmosDB.

**Standard Python3** is recommended; **Anaconda** is not.  Python 2 is not supported.

The following software is also strongly recommended:
- **A mongo UI client** - [Studio 3T](https://studio3t.com), etc.
- **Azure Storage Explorer** - See https://azure.microsoft.com/en-us/features/storage-explorer/
- **A Text Edior** - such as [Visual Studio Code](https://code.visualstudio.com)

Additionally:
- [Docker](https://www.docker.com/products/docker-desktop) and 
[docker-compose](https://docs.docker.com/compose/install/) 
if you wish to run the reference MongoDB locally as a container.

## Copy this git repository to your source control 

Next, create **your own copy** of this repository.  There are at least two ways do
do this.  First, in GitHub, you can simply **fork** this repository.

Alternatively, choose an appropriate directory on your laptop to clone this repository to,
as follows:

```
$ git clone https://github.com/Azure-Samples/azure-cosmos-db-mongo-migration
$ cd azure-cosmos-db-mongo-migration
$ rm -rf .git/
```

Note how we execute **rm -rf .git/** to disconnect from the original GitHub
repository.  Copy the remaining files to **YOUR repository**.

You'll be spending a lot of time in the **m2c directory** (for Mongo-to-Cosmos) within
the repo root directory, including creating a python virtual environment as described next.

## Python Virtual Environment

Though Python is a cross-platform language and runtime, there are many ways to
use and configure it.  A Python **Virtual Environment** is a sandboxed set of libraries
defined with a **requirements.txt** file, and there are multiple ways to create 
python virtual environments - venv, pyenv, etc.

For the development of this project, the [pyenv](https://github.com/pyenv/pyenv) program
is used.  You'll see several **pyenv.sh** scripts in this repo.

However, on your computer, simply create python virtual environment with your tool-of-choice,
and install the **requirements.txt** file(s) found in this repo, such as in the **m2c/** directory.

## Create an Azure Service Principal

If you plan on executing parts of the migration process on an Azure Virtual Machine
then you'll need to create a **Service Principal** as described on this documentation page: 
https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli

From your Development Workstation, run the following command to login:

```
$ az login
```

Next, set and display your Azure Subscription.  You may already have access to several, 
so use the Azure Subscription pertinent to this migration:

```
$ az account set --subscription $AZURE_SUBSCRIPTION_ID
$ az account show
```

Confirm that the "az account show" output displays the "id" value of your
chosen Azure Subscription.

Next, create a **Service Principal (SP)** .  The name MongoToCosmosMigration in this example 
isn't pertinent; choose a name that's consistent with you organization standards.
This creates a SP with the default role of 'Contributor'.

```
$ az ad sp create-for-rbac --name MongoToCosmosMigration
```

**Capture the JSON output of this command - you set these values in env.sh, below.**.  These Service Principal environment variable values will be referenced in generated
script **az_login_sp.sh** used later in the migration process.

Note that the **az login** command allows you to login either from an interactive
web browser with a given code, or in a non-interactive manner with a Service Principal.
When executing "az login" in a VM terminal session, then the Service Principal approach
must be used.

## Environment Variables (env.sh)

This project uses environment variables extensively.  Configuring a system using environment 
variable is generally a best-practice in IT, and is one of the tenets of 
[The Twelve Factor App](https://12factor.net).  Environment Variables are also extensively
used in Azure - such as in App Service, Azure Container Instances, and Azure Kubernetes Service.

Environment Variables are used for general configuration values, as well as for **secrets**
such as database connection strings.

A critical file in this project is **env.sh**, shown below.  This file is **sourced** by
the other scripts in this repo so as to **export** environment variables to those scripts.

**You'll need to edit the env.sh file (shown below) for your particular configuration**. 

**All of the environment variables in env.sh are critical, so please take some time to understand this file.**

```
TODO - repopulate
```

All of the environment variables used by this project begin with **M2C_**, and it
is **required** that you set each of these with **YOUR** particular values.

Note how, for example, on my system I set the value of the M2C_ variables
with **other environment variables defined in my system**, such as 
AZURE_M2C_STORAGE_CONNECTION_STRING.
