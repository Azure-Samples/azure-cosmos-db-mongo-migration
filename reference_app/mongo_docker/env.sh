#!/bin/bash

# This script is 'sourced' by other scripts in this directory
# to define common environment variables.
# Chris Joakim, Microsoft, October 2021

# Source Database
export DOCKER_MONGODB_URL="localhost:27017"
export DOCKER_MONGODB_SSL="false"  # true or false
export DOCKER_MONGODB_HOST="localhost"
export DOCKER_MONGODB_PORT="27017"
export DOCKER_MONGODB_USER="root"
export DOCKER_MONGODB_PASS="rootpassword"
