#!/bin/bash

# Bash shell script to login with the az CLI using your Service Principal (SP).
#
# Generated on:  2021-10-26 19:28:58 UTC
# Template:      az_login_sp.txt

source ./env.sh

echo 'logging in with service principal ...'
az login --service-principal \
    --username $M2C_SP_APP_ID \
    --password $M2C_SP_PASSWORD \
    --tenant   $M2C_SP_TENANT

echo 'setting subscription ...'
az account set --subscription $M2C_SUBSCRIPTION_ID

echo 'showing az account ...'
az account show

echo 'done'