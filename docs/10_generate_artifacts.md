# 10 - Generate Artifacts

**This step will generate high-quality code and file artifacts that can be used "as-is" during migration execution; no manual editing of these artifacts is required.**

**This step is typically executed from a Developer laptop.**

There are two execptions to this no-editing-required rule:
1) The target database ddl or index files, described below.
2) The Azure Data Factory artifacts.  The ADF artifacts can be used as-is.  However, there are some minor
manual steps you must do in ADF in the Azure Portal to fully configure them.

There are two main categories of generated artifacts - **shell scripts**, and **Azure Data Factory**
JSON files.  These are written to the **$M2C_APP_ARTIFACTS_DIR/shell** and 
**$M2C_APP_ARTIFACTS_DIR/adf** directories, respectively.

As mentioned in section [01 - Project Implementation](01_project_implementation.md), the
artifacts are generated with python, the Jinja2 library, and the templates in the m2c/templates directory.
The generated artifacts, where possible (i.e. - the non-JSON file), contain a comment which states how
the artifact was generated and with which template.

You'll later need to **create a Python Virtual Environment in the generated artifacts/shell directory**
to actually execute some of these generated scripts.
See sections [03 - Development Computer Setup](03_development_computer_setup.md) and
[12 - Create the Azure Storage Containers](12_create_the_azure_storage_containers.md), which
describe this process.

---

## "Secrets", Artifacts, Source-Control

**The generated artifacts do not contain your "secret" environment variable values; they only refer to them by name.**

The generated artifacts should be put into **your** source-control system, such as **git or Azure DevOps**.

Your artifact repo can then be cloned to an **Azure Virtual Machine**, where the generated shell scripts
can be executed.

---

## Execute script generate_artifacts.sh

In the **m2c/** directory, execute this script.

Note that it will warn you that it will overwrite any previously generated artifacts;
you much type 'yes' or 'y' to proceed.  The output below is for the reference application.

```
$ ./generate_artifacts.sh

This process will delete all previously generated artifacts, then recreate them.
Do you wish to proceed - delete and regenerate? yes

ensuring target artifact directories exist ...
deleting previous generated artifacts ...
rm: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/*.*: No such file or directory
copying core files to templates ...
generating artifacts ...
generate_artifacts olympics ['main.py', 'generate_artifacts', 'olympics', '--all']
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/olympics_mongoexports.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/create_blob_containers.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/env.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/pyenv.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/storage.py
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/requirements.in
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/requirements.txt
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/olympics_python_mongoexport_uploads.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/olympics_az_cli_mongoexport_uploads.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_all.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_countries.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1896_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1900_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1904_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1906_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1908_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1912_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1920_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1924_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1924_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1928_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1928_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1932_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1932_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1936_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1936_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1948_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1948_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1952_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1952_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1956_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1956_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1960_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1960_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1964_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1964_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1968_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1968_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1972_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1972_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1976_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1976_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1980_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1980_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1984_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1984_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1988_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1988_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1992_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1992_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1994_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1996_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g1998_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g2000_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g2002_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g2004_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g2006_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g2008_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g2010_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g2012_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g2014_winter.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_g2016_summer.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_olympics_games.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/linkedService/M2CMigrationBlobStorage.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/linkedService/M2CMigrationCosmosDB_olympics.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__olympics__games.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__olympics__locations.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__travel__airlines.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__travel__airports.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__travel__countries.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__travel__planes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__travel__routes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__olympics__games.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__olympics__locations.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__travel__airlines.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__travel__airports.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__travel__countries.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__travel__planes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__travel__routes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_olympics_games.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_olympics_locations.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_travel_airlines.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_travel_airports.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_travel_countries.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_travel_planes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_travel_routes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_olympics_games.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_olympics_locations.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_travel_airlines.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_travel_airports.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_travel_countries.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_travel_planes.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_travel_routes.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/olympics_cosmos_db_containers_az_cli.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/mongo/mongo_indexes_olympics_db.ddl
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/mongo_indexes_olympics_db.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/mongo/mongo_indexes_travel_db.ddl
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/mongo_indexes_travel_db.sh
generate_artifacts openflights ['main.py', 'generate_artifacts', 'openflights', '--all']
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/openflights_mongoexports.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/create_blob_containers.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/env.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/pyenv.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/storage.py
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/requirements.in
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/requirements.txt
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/openflights_python_mongoexport_uploads.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/openflights_az_cli_mongoexport_uploads.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_openflights_all.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_openflights_airlines.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_openflights_airports.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_openflights_countries.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_openflights_planes.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/wrangle_openflights_routes.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/linkedService/M2CMigrationBlobStorage.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/linkedService/M2CMigrationCosmosDB_travel.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__olympics__games.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__olympics__locations.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__travel__airlines.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__travel__airports.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__travel__countries.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__travel__planes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/blob__travel__routes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__olympics__games.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__olympics__locations.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__travel__airlines.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__travel__airports.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__travel__countries.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__travel__planes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/dataset/cosmos__travel__routes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_olympics_games.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_olympics_locations.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_travel_airlines.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_travel_airports.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_travel_countries.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_travel_planes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/adf/pipeline/pipeline_copy_to_travel_routes.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_olympics_games.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_olympics_locations.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_travel_airlines.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_travel_airports.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_travel_countries.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_travel_planes.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/adf_pipeline_copy_to_travel_routes.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/travel_cosmos_db_containers_az_cli.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/mongo/mongo_indexes_olympics_db.ddl
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/mongo_indexes_olympics_db.sh
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/mongo/mongo_indexes_travel_db.ddl
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell/mongo_indexes_travel_db.sh
replicating scripts
copying to /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/artifacts/shell ...
copying the mapping file(s) ...
done
making generated scripts executable ...
done
```

---

## mongoexport Scripts

Sample:

```
#!/bin/bash

# Bash shell script to export each source collection via mongoexport.
#
# Database Name: olympics
# Generated on:  2021-06-13 12:04:54 UTC
# Template:      mongoexport_script.txt

source env.sh

mkdir -p data/source/mongoexports

echo ''
echo 'mongoexporting - database: olympics container: countries'
mongoexport --authenticationDatabase admin -u $M2C_SOURCE_MONGODB_USER -p $M2C_SOURCE_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection countries \
    --out /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/olympics/olympics__countries.json
     # no --ssl

echo ''
echo 'mongoexporting - database: olympics container: g1896_summer'
mongoexport --authenticationDatabase admin -u $M2C_SOURCE_MONGODB_USER -p $M2C_SOURCE_MONGODB_PASS --uri mongodb://@localhost:27017 \
    --db olympics \
    --collection g1896_summer \
    --out /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/olympics/olympics__g1896_summer.json
     # no --ssl

...
```

---

## Storage Container Scripts

Sample; create_blob_containers.sh

```
#!/bin/bash

# Bash shell script to create, the list, the blob containers for this migration.
#
# Generated on: 2021-06-13 12:04:55 UTC
# Generated by: artifact_generator.py gen_python_create_containers()
# Template:     create_blob_containers.txt

source env.sh

python storage.py create_blob_container olympics-games-adf
python storage.py create_blob_container olympics-locations-adf
python storage.py create_blob_container olympics-raw
python storage.py create_blob_container openflights-raw
python storage.py create_blob_container travel-airlines-adf
python storage.py create_blob_container travel-airports-adf
python storage.py create_blob_container travel-countries-adf
python storage.py create_blob_container travel-planes-adf
python storage.py create_blob_container travel-routes-adf

python storage.py list_blob_containers

echo 'done'
```

---

## mongoexport File Upload Scripts

Two equivalent sets of mongoexport file upload scripts are created; one uses
**python and Azure Storage SDK** while the other uses the **az CLI**.  Either can
be used depending on customer preferences.

Python Sample:

```
#!/bin/bash

# Bash shell script to upload mongoexport blobs to Azure Storage with Python3.
#
# Database Name: openflights
# Generated on:  2021-06-13 12:04:55 UTC
# Generated by:  artifact_generator.py gen_python_uploads()
# Template:      blob_uploads_python.txt

source env.sh

# Uncomment, as necessary, to delete and recreate the storage container:
# python storage.py delete_blob_container openflights-raw
# sleep 10
# python storage.py create_blob_container openflights-raw
# sleep 10

echo '---'
date
python storage.py upload_blob /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__airlines.json openflights-raw openflights__airlines.json

echo '---'
date
python storage.py upload_blob /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__airports.json openflights-raw openflights__airports.json

...
```

az CLI Sample:

```
#!/bin/bash

# Bash shell script to upload mongoexport blobs to Azure Storage with the az CLI.
#
# Database Name: openflights
# Generated on:  2021-06-13 12:04:55 UTC
# Generated by:  artifact_generator.py gen_az_cli_uploads()
# Template:      blob_uploads_az_cli.txt

source env.sh

# Uncomment as necessary:
# echo 'acct: '$M2C_STORAGE_ACCOUNT
# echo 'key:  '$M2C_STORAGE_KEY

echo '---'
echo 'uploading /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__airlines.json to openflights-raw ...'
date 
az storage blob upload \
  --container-name openflights-raw \
  --file /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__airlines.json \
  --name  openflights__airlines.json \
  --account-name $M2C_STORAGE_ACCOUNT \
  --account-key $M2C_STORAGE_KEY

echo '---'
echo 'uploading /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__airports.json to openflights-raw ...'
date 
az storage blob upload \
  --container-name openflights-raw \
  --file /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/openflights/openflights__airports.json \
  --name  openflights__airports.json \
  --account-name $M2C_STORAGE_ACCOUNT \
  --account-key $M2C_STORAGE_KEY

...
```

---

## Wrangling Scripts

Scripts to wrangle **each** mongoexport file, as well as **all** mongoexport files,
for a source database are created.  For example:

```
reference_app/artifacts/shell/wrangle_openflights_airlines.sh
reference_app/artifacts/shell/wrangle_openflights_airports.sh
reference_app/artifacts/shell/wrangle_openflights_countries.sh
reference_app/artifacts/shell/wrangle_openflights_planes.sh
reference_app/artifacts/shell/wrangle_openflights_routes.sh

reference_app/artifacts/shell/wrangle_openflights_all.sh   <-- executes each of the above
```

Sample, wrangle_openflights_airlines.sh:

```
#!/bin/bash

# Bash shell script to wrangle/transform a raw mongoexport file.
#
# Database Name: openflights
# Generated on:  2021-06-13 12:32:30 UTC
# Template:      wrangle_one.txt

source ./env.sh

mkdir -p tmp/openflights/out
mkdir -p out/openflights

# This script does the following:
# 1) Downloads blob openflights__airlines.json from container openflights-raw
#    to local file tmp/openflights/openflights__airlines.json
# 2) Wrangle/transform the downloaded blob, producing local file 
#    tmp/openflights/openflights__airlines__wrangled.json
# 3) Uploads the wrangled file to storage container openflights-adf
# 4) Delete the downloaded and wrangled file, as the host VM may have limited storage
#
# Note: this script is executed by script openflights_wrangle_all.sh

python wrangle.py transform_blob \
    --db openflights \
    --source-coll  airlines \
    --in-container openflights-raw \
    --blobname openflights__airlines.json \
    --filename tmp/openflights/openflights__airlines.json \
    --outfile  tmp/openflights/openflights__airlines__wrangled.json \
    --out-container travel-airlines-adf $1 $2 $3 

echo ''
echo 'first line of input file:'
head -1 tmp/openflights/openflights__airlines.json

echo ''
echo 'first line of output file:'
head -1 tmp/openflights/openflights__airlines__wrangled.json

echo 'deleting the downloaded and wrangled files to save disk space...'
rm tmp/openflights/openflights__airlines.json
rm tmp/openflights/openflights__airlines__wrangled.json

echo 'done' 
```

---

## Create Cosmos Database and Containers scripts

Sample; travel_cosmos_db_containers_az_cli.sh

Note that the name "travel_" prefix refers to the **target database**, per your **mappings**,
rather than the source database.

```
#!/bin/bash

# Bash shell script to create an autoscaled database, with containers
# in a CosmosDB/Mongo account.
#
# Database Name: travel
# Generated on:  2021-06-13 12:32:30 UTC
# Generated by:  artifact_generator.py gen_target_cosmos_az_create()
# Template:      cosmos_db_containers_az_cli.txt

source env.sh

echo 'creating cosmos db: travel'
az cosmosdb mongodb database create \
    --resource-group $M2C_RG \
    --account-name $M2C_COSMOS_MONGODB_ACCT \
    --name travel \
    --max-throughput 5000

echo 'creating cosmos collection: airlines'
az cosmosdb mongodb collection create \
    --resource-group $M2C_RG \
    --account-name $M2C_COSMOS_MONGODB_ACCT \
    --database-name travel \
    --name airlines \
    --shard pk

echo 'creating cosmos collection: airports'
az cosmosdb mongodb collection create \
    --resource-group $M2C_RG \
    --account-name $M2C_COSMOS_MONGODB_ACCT \
    --database-name travel \
    --name airports \
    --shard pk

echo 'creating cosmos collection: countries'
az cosmosdb mongodb collection create \
    --resource-group $M2C_RG \
    --account-name $M2C_COSMOS_MONGODB_ACCT \
    --database-name travel \
    --name countries \
    --shard pk

echo 'creating cosmos collection: planes'
az cosmosdb mongodb collection create \
    --resource-group $M2C_RG \
    --account-name $M2C_COSMOS_MONGODB_ACCT \
    --database-name travel \
    --name planes \
    --shard pk

echo 'creating cosmos collection: routes'
az cosmosdb mongodb collection create \
    --resource-group $M2C_RG \
    --account-name $M2C_COSMOS_MONGODB_ACCT \
    --database-name travel \
    --name routes \
    --shard pk

echo 'done'
```

---

## Cosmos/Mongo Index Files

Two sets of files are generated here, a "ddl" file that defines the indexes,
and a shell script that executes the ddl file.

For example:
```
reference_app/artifacts/shell/mongo/mongo_indexes_olympics_db.ddl
reference_app/artifacts/shell/mongo/mongo_indexes_travel_db.ddl
reference_app/artifacts/shell/mongo_indexes_olympics_db.sh
reference_app/artifacts/shell/mongo_indexes_travel_db.sh
```

Since this migrator project has no knowledge of the query patterns in your application, 
**you are required to edit the ddl files to contain the indexes that are appropriate for your app.**

Sample; mongo_indexes_travel_db.sh:

```
#!/bin/bash

# bash script to execute the mongo command-line program, redirecting
# in a "ddl" file to indexes for your collections in the Cosmos/Mongo database.
# TODO: the customer needs to manually edit the input ddl file with the indexes.
#
# Generated on: 2021-06-13 12:32:30 UTC
# Generated by: artifact_generator.py gen_target_cosmos_mongo_indexes()
# Template:     mongo_database_indexes.txt

source env.sh

echo 'init database travel ...'
mongo $M2C_COSMOS_MONGO_CONN_STRING --ssl < mongo/mongo_indexes_travel_db.ddl
```

Sample; mongo/mongo_indexes_travel_db.ddl

```
// MongoDB "DDL" create the indexes in the "travel" database
// and its collections.
//
// Generated on: 2021-06-13 12:32:30 UTC
// Generated by: artifact_generator.py gen_target_cosmos_mongo_indexes()
// Template:     mongo_database_indexes.ddl
// TODO:         the customer needs to manually edit the this file

use travel

// db.airlines.ensureIndex({"some_attribute" : 1}, {"unique" : false})

// db.airports.ensureIndex({"some_attribute" : 1}, {"unique" : false})

// db.countries.ensureIndex({"some_attribute" : 1}, {"unique" : false})

// db.planes.ensureIndex({"some_attribute" : 1}, {"unique" : false})

// db.routes.ensureIndex({"some_attribute" : 1}, {"unique" : false})

show collections
```

---

## ADF JSON Artifacts

The Azure Data Factory artifacts will be written to this target directory structure
within your $M2C_APP_DIR.  ADF **LinkedService**, **Dataset**, and **Pipeline**
JSON artifacts are created.

```
└── reference_app
    ├── artifacts
    │   ├── adf
    │   │   ├── dataset
    │   │   ├── linkedService
    │   │   └── pipeline
```

This will be discussed further in section [15 - ADF Setup with Git Source Control](15_adf_setup_with_git_source_control.md)

LinkedService Sample, Blob Storage:

```
{
	"name": "M2CMigrationBlobStorage",
	"type": "Microsoft.DataFactory/factories/linkedservices",
	"properties": {
		"annotations": [],
		"type": "AzureBlobStorage",
		"typeProperties": {
			"connectionString": "",
			"encryptedCredential": ""
		}
	}
}
```

LinkedService Sample, CosmosDB Database:

```
{
	"name": "M2CMigrationCosmosDB_olympics",
	"type": "Microsoft.DataFactory/factories/linkedservices",
	"properties": {
		"annotations": [],
		"type": "CosmosDbMongoDbApi",
		"typeProperties": {
			"connectionString": "",
			"database": "olympics",
			"encryptedCredential": ""
		}
	}
}
```


Blob Dataset Sample:

```
{
    "name": "blob__olympics__games",
    "properties": {
        "linkedServiceName": {
            "referenceName": "M2CMigrationBlobStorage",
            "type": "LinkedServiceReference"
        },
        "annotations": [],
        "type": "Json",
        "typeProperties": {
            "location": {
                "type": "AzureBlobStorageLocation",
                "container": "olympics-games-adf",
                "fileName": "*.json"
            }
        },
        "schema": {}
    }
}
```

CosmosDB Dataset Sample:

```
{
    "name": "cosmos__olympics__games",
    "properties": {
        "description": "target container",
        "linkedServiceName": {
            "referenceName": "M2CMigrationCosmosDB_olympics",
            "type": "LinkedServiceReference"
        },
        "annotations": [],
        "type": "CosmosDbMongoDbApiCollection",
        "schema": [],
        "typeProperties": {
            "collection": "games"
        }
    },
    "type": "Microsoft.DataFactory/factories/datasets"
}
```

Pipeline Sample:

```

{
	"name": "pipeline_copy_to_olympics_games",
	"properties": {
		"activities": [
			{
				"name": "copy_blob__olympics__games",
				"type": "Copy",
				"dependsOn": [ 
					
				],
				"policy": {
					"timeout": "7.00:00:00",
					"retry": 0,
					"retryIntervalInSeconds": 30,
					"secureOutput": false,
					"secureInput": false
				},
				"userProperties": [
					{
						"name": "generated_at",
						"value": "2021-06-13 12:32:30 UTC"
					}
				],
				"typeProperties": {
					"source": {
						"type": "JsonSource",
						"storeSettings": {
							"type": "AzureBlobStorageReadSettings",
							"recursive": true,
							"wildcardFileName": "*.json",
							"enablePartitionDiscovery": false
						},					
						"formatSettings": {
							"type": "JsonReadSettings"
						}
					},
					"sink": {
						"type": "CosmosDbMongoDbApiSink",
						"writeBatchTimeout": "01:00:00",
						"writeBehavior": "upsert"
					},
					"enableStaging": false
				},
				"inputs": [
					{
						"referenceName": "blob__olympics__games",
						"type": "DatasetReference"
					}
				],
				"outputs": [
					{
						"referenceName": "cosmos__olympics__games",
						"type": "DatasetReference"
					}
				]
			}
			

		],
		"annotations": [],
		"lastPublishTime": "2021-05-21T21:01:43Z"
	},
	"type": "Microsoft.DataFactory/factories/pipelines"
}
```
