# 04 - Initial Customer Edits

Before Source Database Metadata Extraction happens, you need to first edit env.sh
and also specify the list of source databases.

**This step is typically executed from a Developer laptop.**

## env.sh

As described in [03 - Development Computer Setup](03_development_computer_setup.md)
it is critical to edit file **env.sh** per your environment.

Three of these are further described below:

```
export M2C_APP_DIR=$M2C_REF_APP_DIR
export M2C_APP_ARTIFACTS_DIR=$M2C_REF_APP_DIR"/artifacts"
export M2C_APP_DATA_DIR=$M2C_REF_APP_DIR"/data"
```

The idea here is that you set **M2C_APP_DIR**, **M2C_APP_ARTIFACTS_DIR**, and **M2C_APP_DATA_DIR** to some directories on your computer where you will edit
some files, and also where the generated artifacts will be written to.

## Create Directories

Given that you set **M2C_APP_DIR** in **env.sh**, as described above, execute
the following script to create these directories on your computer:

```
$ cd m2c
$ ./create_directories.sh   # this is in same directory as env.sh
```

**create_directories.sh** will execute the following:

```
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
```

## Databases List - migrated_databases_list.txt

Edit file **$M2C_APP_DATA_DIR/metadata/migrated_databases_list.txt** to the list of your
current MongoDB databases that you wish to migrate to CosmosDB.  These databased
reside at the **M2C_SOURCE_MONGODB_** variables that you set in **env.sh**.

For example, to export the two reference databases, edit file migrated_databases_list.txt
to have these two lines:

```
olympics
openflights
```
