#!/bin/bash

# Bash shell scripts to execute the pytest-based unit, tests with code coverage.
# Chris Joakim, Microsoft, October 2021

source bin/activate
source env.sh

# echo 'checking the source code with flake8 ...'
# flake8 cjcc --ignore F401

echo 'executing unit tests with code coverage ...'
pytest -v --cov=pysrc/ --cov-report html tests/
