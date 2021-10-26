#!/bin/bash

# Bash shell that defines parameters and environment variables used in
# this app, and is "sourced" by the other scripts in this directory.
# Chris Joakim, Microsoft, August 2021

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
export uvm_name="m2cmigrationvm2"
export uvm_publisher='Canonical'
export uvm_offer='UbuntuServer'
export uvm_sku='20.04-LTS'
export uvm_version='latest'
export uvm_image='UbuntuLTS'
#export uvm_image=""$uvm_publisher":"$uvm_offer":"$uvm_sku":"$uvm_version # Values from: az vm image list
export uvm_size="Standard_D3_v2"  # Values from: az vm list-sizes, Default: Standard_DS1_v2
export uvm_datasizegb="1024"
export uvm_user=$AZURE_UVM_USER   # cjoakim
export uvm_ssh_keys=$AZURE_UVM_PUBLIC_SSH_KEY  # $HOME/<user>/.ssh/<name>.pub
