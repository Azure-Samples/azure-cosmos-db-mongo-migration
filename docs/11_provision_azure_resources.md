# 11 - Provision Azure Resources

The **m2c/az** directory contains shell scripts.

**This step is typically executed from a Developer laptop.**

First edit file **azconfig.sh**, shown below, for your migration.
Set your Azure Subscription, Region, Resource Group, and Resource names - 
please do not use **cjoakim** in your names!

```
TODO - repopulate
```

## Storage

Execute script **storage.sh**

Note: this only creates the Azure Storage account; not the blob containers.
See section [12 - Create the Azure Storage Containers](12_create_the_azure_storage_containers.md)

## Azure Data Factory

Execute script **adf1.sh**

## CosmosDB with Mongo API

Execute script **cosmos_mongo.sh**

Note: this only creates the CosmosDB account; not the databases and collections.
See section [13 - Create the CosmosDB Target Databases and Containers](13_create_the_cosmosdb_target_databases_and_containers.md)

## Virtual Machine

### Provision 

Execute script **/uvm.sh create**

```
$ ./uvm.sh create
creating UVM rg: cjoakimm2c
creating UVM: m2cmigrationvm1
INFO: Use existing SSH public key file: ....
INFO: Command ran in 94.545 seconds (init: 0.137, invoke: 94.408)
done
```

### Networking

In Azure Portal, go to the VM created above.  Record the **Public IP Address** value.

Then, in the **Networking** panel of your VM, set the 
**Inbound Port Rule for port 22 to the IP Address of your Laptop/Workstation**, and click Save.
This will ensure ssh access to the VM only from your IP.

### ssh into you VM 

```
$ ssh -A <user>@<vm-ip-address-per-azure-portal>
```

### Install the az CLI


```
$ curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

### Clone your repo

**Clone YOUR repo, with your generated artifacts, etc.**

This example show cloning this repo and the reference app repos:

```
$ cd ~           <-- change to some migration-root directory of your choice on the VM

$ which git
/usr/bin/git     <-- excellent, git is already installed on the VM

$ git clone https://github.com/Azure-Samples/azure-cosmos-db-mongo-migration
```

### Install Necessary Software

**Ubuntu Linux Virtual Machines are recommended, with the following installed:**

- **Azure CLI (az)** - See https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
- **python3**  - The project was developed and tested with python 3.8.6.
- **python3-pip** - python package manager
- **python3-venv** - python virtual environment tool
- **mongo client, mongoexport, mongoimport** - from MongoDB Community Edition
- **jq** - JSON validator and pretty-printer
- **docker**
- **docker-compose**

**Note: Standard Python** is strongly recommended; **Anaconda** is not.

See the **standard-installs.sh** script in the **m2c/az/uvm/scripts/** directory of
this repo.  This script can be executed on your Ubuntu Linux Virtual Machine
to install the above software which is necessary for the migration process.
