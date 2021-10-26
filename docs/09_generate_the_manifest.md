# 09 - Generate the Manifest

You can think of the **manifest files** as a **"shipping manifest"**, as it
describes each source database/collection combination, and its
**"journey"** through the migration process from source to target.

This file weaves together data from both the extracted **source database metadata**, as well
as the **customer-edited mappings** file(s) to create a combined view.

Like the **metadata** files, the **manifest** file is **not intended to be edited**.
It is used in the next step - **artifact generation**, described on the next page.

**This step is typically executed from a Developer laptop.**

## Execute script generate_manifest.sh

In the **m2c/** directory, execute this script:

```
$ ./generate_manifest.sh

generating manifest ...
databases_list: ['olympics', 'openflights']
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/metadata/manifest.csv
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/metadata/manifest.json

Note: the generated 'manifest.json' is used in code generation, so please don't edit it.

done
```

## JSON Sample

See file **reference_app/data/metadata/manifest.json** in the sibling GitHub repository.

For example, the manifest entry for one container looks like this:

```
    ...
    {
      "source_db": "olympics",
      "source_coll": "g1896_summer",
      "doc_count": "760",
      "avg_doc_size": "323",
      "target_db": "olympics",
      "target_coll": "games",
      "partition_key": "pk",
      "blob_name": "olympics__g1896_summer.json",
      "raw_storage_container": "olympics-raw",
      "adf_storage_container": "olympics-games-adf",
      "adf_blob_doc_count": "-1",
      "adf_blob_dataset_name": "blob__olympics__games",
      "adf_cosmos_dataset_name": "cosmos__olympics__games",
      "adf_pipeline_name": "pipeline_copy_to_olympics_games",
      "mongoexports_dir": "/Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/olympics",
      "mongoexport_file": "/Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/mongoexports/olympics/olympics__g1896_summer.json",
      "wrangle_script_name": "wrangle_olympics_g1896_summer.sh",
      "wrangled_outfile": "tmp/olympics/olympics__g1896_summer__wrangled.json",
      "local_file_path": "tmp/olympics/olympics__g1896_summer.json"
    },
    ...
```

## Excel

A subset of these JSON attributes are also in generated CSV file **manifest.csv**.
You can open this file in **Excel**, which can be helpful to visualize and track your migration.

This CSV file can be edited after generation, while the manifest.json file should not be edited.
