#!/bin/bash

# Bash script to create, populate, and activate the python virtual environment
# for this project with pyenv.
# Chris Joakim, Microsoft, July 2021

# These are the only two values that need to change between projects:
venv_name="m2c"
python_version="3.8.6"

echo '=== creating virtualenv '$venv_name
rm .python-version
pyenv virtualenv -f $python_version $venv_name

echo '=== python version'
python3 --version 

echo '=== setting pyenv local ...'
pyenv local $venv_name

echo '=== upgrade pip3 ...'
pip3 install --upgrade pip

echo '=== install pip-tools ...'
pip3 install pip-tools

echo '=== pip3 compile ...'
pip-compile

echo '=== pip3 install ...'
pip3 install -r requirements.txt

echo '=== pip3 list ...'
pip3 list

echo '=== .python-version ...'
cat .python-version

echo 'done'
