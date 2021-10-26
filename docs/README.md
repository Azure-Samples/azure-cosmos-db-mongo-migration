# Project Documentation

## Table of Contents

- [00 - Purpose](00_purpose.md)
- [01 - Project Implementation](01_project_implementation.md)
- [02 - Reference Application](02_reference_application.md)
- [03 - Development Computer Setup](03_development_computer_setup.md)
- [04 - Initial Customer Edits](04_initial_customer_edits.md)
- [05 - Generate Initial Scripts](05_generate_initial_scripts.md)
- [06 - Extract Source Database Metadata](06_extract_source_database_metadata.md)
- [07 - Generate Mapping Files](07_generate_mapping_files.md)
- [08 - Edit the Mapping Files](08_edit_the_mapping_files.md)
- [09 - Generate the Manifest](09_generate_the_manifest.md)
- [10 - Generate Artifacts](10_generate_artifacts.md)
- [11 - Provision Azure Resources](11_provision_azure_resources.md)
- [12 - Create the Azure Storage Containers](12_create_the_azure_storage_containers.md)
- [13 - Create the CosmosDB Target Databases and Containers](13_create_the_cosmosdb_target_databases_and_containers.md)
- [14 - CosmosDB Container Indexing](14_cosmosdb_container_indexing.md)
- [15 - ADF Setup with Git Source Control](15_adf_setup_with_git_source_control.md)
- [16 - Partition Key Distribution Analysis](16_pk_distribution.md)
- [18 - Execute Migration](18_execute_migration.md)
- [20 - Roadmap](20_roadmap.md)

---

## Summary of Actions and Scripts to Execute

This section summarizes the aboe content pages.

- Development Computer Setup, see [03 - Development Computer Setup](03_development_computer_setup.md)
- Copy/clone/fork this repo to your private source control system
- Create Service Principal, see [03 - Development Computer Setup](03_development_computer_setup.md)
- Edit **env.sh** - the environment variables script, see [03 - Development Computer Setup](03_development_computer_setup.md)
- Execute **create_directories.sh** for output directories, see [04 - Initial Customer Edits](04_initial_customer_edits.md)
- Edit file **$M2C_APP_DATA_DIR/metadata/migrated_databases_list.txt** for your list of databases, see [04 - Initial Customer Edits](04_initial_customer_edits.md)
- Execute **generate_initial_scripts.sh**, see [05 - Generate Initial Scripts](05_generate_initial_scripts.md)
- Execute **extract_metadata.sh** for source database information, see [06 - Extract Source Database Metadata](06_extract_source_database_metadata.md)
- Execute **generate_mapping_files.sh** for source-to-target-DB mappings, see [07 - Generate Mapping Files](07_generate_mapping_files.md)
  - Optionally reimplement **standard_mapping_generator.py** (generates the mapping files for you)
  - Then execute **generate_mapping_files.sh**
- Optionally manually edit the generated mapping files, see [08 - Edit the Mapping Files](08_edit_the_mapping_files.md)
- Execute **generate_manifest.sh**, see [09 - Generate the Manifest](09_generate_the_manifest.md)
- Execute **generate_artifacts.sh**, see [10 - Generate Artifacts](10_generate_artifacts.md)
  - there are several migration strategies:
    - mongoexport + wrangle + Azure Data Factory
    - mongoexport + wrangle + mongoimport
    - mongoexport + wrangle + DotNet Loader
    - In all cases, scripts/artifacts are generated 
- Add all files created above to your source control system 
  - These files in source control may be used on both on-prem and Azure VMs
- Provision Azure Resources, see [11 - Provision Azure Resources](11_provision_azure_resources.md)
  - CosmosDB with Mongo API
  - Ubuntu Linux VM(s)
    - Setup the VM(s)
  - Azure Data Factory, optional per migration strategy 
- Execute the generated **xxx_cosmos_db_containers_az_cli.sh** scripts, where xxx is database name, see [13 - Create the CosmosDB Target Databases and Containers](13_create_the_cosmosdb_target_databases_and_containers.md)
- Execute the generated **mongo_indexes_xxx_db.sh** scripts, where xxx is database name, see [14 - CosmosDB Container Indexing](14_cosmosdb_container_indexing.md)
- Azure Data Factory setup, Optional, see [15 - ADF Setup with Git Source Control](15_adf_setup_with_git_source_control.md)
- Partition Key Analysis is recommended, see [16 - Partition Key Distribution Analysis](16_pk_distribution.md)
- Execute Migrations - there are several strategies for this:
  - mongoexport + wrangle + Azure Data Factory
  - mongoexport + wrangle + mongoimport
  - mongoexport + wrangle + DotNet Loader
  - In all cases, use the generated scripts/
  - The sequence of scripts/processes to execute depends on the migration strategy, in general:
    - create CosmosDB databases and containers, **ddd_cosmos_db_containers_az_cli.sh**
    - create CosmosDB indexes for the containers, **mongo_indexes_ddd_db.sh**
    - import the generated adf/ linked service, dataset, and pipeline json files into Azure Data Factory.  Manually configure these in ADF.
    - execute mongoexports, **ddd_mongoexports.sh** scripts
    - execute blob uploads, **ddd_az_cli_mongoexport_uploads.sh** or **ddd_python_mongoexport_uploads.sh**
    - execute wrangling/transformation/upload scripts:
      - **wrangle_ddd_all.sh** (all containers for the database)
      - **wrangle_ddd_ccc.sh** (individual containers for the database)
      - these wrangle scripts will also upload to CosmosDB per M2C_COSMOS_LOAD_METHOD environment variable
    - Execute the ADF pipelines
    - in the above examples, ddd is a database name and ccc is a container name

