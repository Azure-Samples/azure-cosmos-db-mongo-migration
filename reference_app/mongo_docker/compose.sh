#!/bin/bash

# Alias for docker-compose.
#
# Usage:
# $ ./compose.sh up
# $ ./compose.sh ps
# $ ./compose.sh down
#
# Chris Joakim, Microsoft, October 2021

source env.sh

docker-compose $1
