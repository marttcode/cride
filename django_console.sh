#!/bin/bash

export COMPOSE_FILE=local.yml
echo 'local vars exported'

docker-compose up

#docker rm -f ride_django_1
#docker-compose run --rm --service-ports django
