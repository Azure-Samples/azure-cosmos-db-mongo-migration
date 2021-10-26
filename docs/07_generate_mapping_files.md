# 07 - Generate Mapping Files

This project uses **mapping files**, one per source database, that the customer edits 
**to map the source databases and collections to the target database and its' collections**. 

The mapping files also lets you define standard **built-in** data wrangling, or transformations,
of raw to ADF mongoexport files.

See the exmples in the reference app repo:

```
reference_app/data/metadata/olympics_mapping.json
reference_app/data/metadata/openflights_mapping.json
```

**This step is typically executed from a Developer laptop.**

## Sample

This example from **olympics_mapping.json** shows the mapping for the **g1896_summer**
collection.  The target CosmosDB database and collection are mapped to **olympics** and **games**,
respectively.  These database and container mappings are **required**.

There a number of **optional attribute mappings** as described below.  These optional
fields are **pk_name, pk_logic, doctype_name, doctype_logic, additions, and excludes**.

The **pk_name** defines the CosmosDB partition key attribute name will be **pk**.
The **pk_logic** array lets you define a set of rules to populate that named attribute.
This example shows that the pk will be populated from the **games** attribute in the
raw mongoexport file.

The **doctype_name** and **doctype_logic** are similar to the above pk mappings.
These allow you to add a **document type** attribute to your migrated documents.
The example shows that the **doctype** attribute will be populated from a dynamic
value - the **source_cname** (source database container name).

The **additions** section allows you to add additional attributes to the output
mongoexport files for ADF.  The example shows that the **some_id** attribute will
be added, with a dynamic uuid value.

Lastly, the **excludes** section lets you define attribute names in the input raw mongoexport
file that will be removed, and not ported to CosmosDB.

This documentation page describes just the most common attribute mappings.  Please
see file **pysrc/standard_doc_wrangler.py** for the complete set of declarative
transformations that are available.

Alternatively, you can write your own transformation/wrangler class and use it instead
of standard_doc_wrangler.py.

```
    {
      "name": "g1896_summer",
      "mapping": {
        "target_dbname": "olympics",
        "target_container": "games",
        "wrangling_algorithm": "standard",
        "pk_name": "pk",
        "pk_logic": [
          [
            "attribute",
            "games"
          ]
        ],
        "pk_sep": "-",
        "doctype_name": "doctype",
        "doctype_logic": [
          [
            "dynamic",
            "source_cname"
          ]
        ],
        "doctype_sep": "-",
        "additions": [
          [
            "dynamic",
            "some_id",
            "uuid"
          ]
        ],
        "excludes": [
          "id"
        ]
      }
    },

```

## Execute script generate_mapping_files.sh

In the **m2c/** directory, execute this script:

```
$ ./generate_mapping_files.sh

This process will overlay the mapping files you may have edited.
Do you wish to proceed - regenerate and overlay? yes

file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/metadata/olympics_mapping.json
file written: /Users/cjoakim/github/azure-m2c-wgm-reference-app/reference_app/data/metadata/openflights_mapping.json
done
```

## Write your own Generator

While you can manually edit your own mapping files, it is faster to write software to generate
these mapping files for you.

See python file **standard_mapping_generator.py** in the **m2c/pysrc** directory
and copy and reimplement it as necessary for your migration. 

This class is used in **main.py**, which you can modify to use your mapping generator.
