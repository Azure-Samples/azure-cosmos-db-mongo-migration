#!/bin/bash

# Bash script to create the initial directory structure for the 
# generated application and artifacts.
# Chris Joakim, Microsoft, October 2021

source env.sh

echo 'M2C_APP_DIR is '$M2C_APP_DIR

mkdir -p $M2C_APP_DIR
mkdir -p $M2C_APP_DIR/artifacts
mkdir -p $M2C_APP_DIR/artifacts/adf/dataset
mkdir -p $M2C_APP_DIR/artifacts/adf/linkedService
mkdir -p $M2C_APP_DIR/artifacts/adf/pipeline
mkdir -p $M2C_APP_DIR/artifacts/shell
mkdir -p $M2C_APP_DIR/artifacts/shell/data
mkdir -p $M2C_APP_DIR/artifacts/shell/mongo
mkdir -p $M2C_APP_DIR/artifacts/shell/out
mkdir -p $M2C_APP_DIR/artifacts/shell/pysrc
mkdir -p $M2C_APP_DIR/artifacts/shell/tmp

mkdir -p $M2C_APP_DIR/data
mkdir -p $M2C_APP_DIR/data/metadata

mkdir -p $M2C_APP_DIR/databases

echo 'done; directories created'
