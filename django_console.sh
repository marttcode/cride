export COMPOSE_FILE=local.yml

docker rm -f ride_django_1

docker-compose run --rm --service-ports django

