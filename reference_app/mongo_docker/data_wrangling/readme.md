# Directory: reference_app/mongo_docker/data_wrangling

**Users of this project do NOT need to execute the code in this directory.**

This directory is for the "data wrangling" process that takes the raw
Olympics and Openflights datasets, and converts them into the **mongoimport** 
format for loading into MongoDB.

This process is implemented in Python.

## Execution 

```
$ ./pyenv.sh

$ ./wrangle_olympics_data.sh

$ ./wrangle_openflights_data.sh
```
