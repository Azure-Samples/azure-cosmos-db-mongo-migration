# 05 - Generate Initial Scripts

This section effectively **bootstraps** your migration by generating
three shell scripts.

**This step is typically executed from a Developer laptop.**

## Execute script generate_initial_scripts.sh

In the **m2c/** directory, execute this script:

```
$ ./generate_initial_scripts.sh
```

Which produces the following output:

```
generate_initial_scripts
databases_list: ['olympics', 'openflights']
file written: extract_metadata.sh
file written: generate_mapping_files.sh
file written: generate_artifacts.sh
done
```

This process reads the **migrated_databases_list.txt** file, described in the
previous section, and generates three bash script files shown.

These output files are written to your **m2c/** directory, the same directory
as the executed generate_initial_scripts.sh script itself.
