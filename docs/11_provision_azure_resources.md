# 11 - Provision Azure Resources

The **m2c/az** directory contains shell scripts.

**This step is typically executed from a Developer laptop.**

First edit file **azconfig.sh**, shown below, for your migration.
Set your Azure Subscription, Region, Resource Group, and Resource names - 
please do not use **cjoakim** in your names!

```
#!/bin/bash

# Bash shell that defines parameters and environment variables used in
# this app, and is "sourced" by the other scripts in this directory.
# Chris Joakim, Microsoft, June 2021

# environment variables for provisioning:

export subscription=$AZURE_SUBSCRIPTION_ID
export user=$USER
export primary_region="eastus"
export primary_rg="cjoakimm2c"

# adf1 is intended to be the "production" ADF with git integration
# adf2 is intended to be the "ad-hoc, exploration" ADF with no git integration
export adf_region=$primary_region
export adf_rg=$primary_rg
export adf1_name="cjoakimm2cadf1"
export adf2_name="cjoakimm2cadf2"
#
export cosmos_mongo_region=$primary_region
export cosmos_mongo_rg=$primary_rg
export cosmos_mongo_acct_name="cjoakimm2ccosmosmongo"
export cosmos_mongo_acct_consistency="Session"    # {BoundedStaleness, ConsistentPrefix, Eventual, Session, Strong}
export cosmos_mongo_version="4.0"
#
export storage_region=$primary_region
export storage_rg=$primary_rg
export storage_name="cjoakimm2cstorage"
export storage_kind="BlobStorage"     # {BlobStorage, BlockBlobStorage, FileStorage, Storage, StorageV2}]
export storage_sku="Standard_LRS"     # {Premium_LRS, Premium_ZRS, Standard_GRS, Standard_GZRS, , Standard_RAGRS, Standard_RAGZRS, Standard_ZRS]
export storage_access_tier="Hot"      # Cool, Hot
#
export uvm_rg=$primary_rg
export uvm_region=$primary_region
export uvm_name="m2cmigrationvm1"
export uvm_publisher='Canonical'
export uvm_offer='UbuntuServer'
export uvm_sku='18.04-LTS'
export uvm_version='latest'
export uvm_image=""$uvm_publisher":"$uvm_offer":"$uvm_sku":"$uvm_version # Values from: az vm image list
export uvm_size="Standard_D3_v2"  # Values from: az vm list-sizes, Default: Standard_DS1_v2
export uvm_datasizegb="1024"
export uvm_user=$AZURE_UVM_USER   # cjoakim
export uvm_ssh_keys=$AZURE_UVM_PUBLIC_SSH_KEY  # $HOME/<user>/.ssh/<name>.pub
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

$ git clone git@github.com:cjoakim/azure-m2c-wgm.git
 - or -
$ git clone https://github.com/cjoakim/azure-m2c-wgm.git

$ git clone git@github.com:cjoakim/azure-m2c-wgm-reference-app.git
 - or -
$ git clone https://github.com/cjoakim/azure-m2c-wgm-reference-app.git
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
