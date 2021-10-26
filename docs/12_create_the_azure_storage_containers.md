# 12 - Create the Azure Storage Containers

**This step is typically executed from a Developer laptop.**

## Python Virtual Environment

As described in section [03 - Development Computer Setup](03_development_computer_setup.md)
you'll have to similarly create a python virtual environment in the locatation
where you execute the generated shell scripts.  Use the requirements.txt file in this directory.

## Execute script create_blob_containers.sh

```
$ ./create_blob_containers.sh

...
1 olympics-games-adf
2 olympics-locations-adf
3 olympics-raw
4 openflights-raw
5 test
6 travel-airlines-adf
7 travel-airports-adf
8 travel-countries-adf
9 travel-planes-adf
10 travel-routes-adf
done
```

You can execute this script several times.  It will show errors like this if a
storage container already exists.  These errors may be ignored.

```
Traceback (most recent call last):
  File "storage.py", line 54, in create_container
    container_client.create_container()
  File "/Users/cjoakim/.pyenv/versions/m2cshell/lib/python3.8/site-packages/azure/core/tracing/decorator.py", line 83, in wrapper_use_tracer
    return func(*args, **kwargs)
azure.core.exceptions.ResourceExistsError: The specified container already exists.
RequestId:4fb1cc47-101e-00a9-1f57-60948f000000
Time:2021-06-13T13:24:42.5977549Z
ErrorCode:ContainerAlreadyExists
```

