#!/bin/sh

echo "Waiting for Postgres init..."

# netcat will send empty traffic to the users-db host
# while that is not able to connect, sleep and try again
# then finish
while ! nc -z users-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started on port 5432"

# now that we have made connection with the pg db
# we can run the manage script
python manage.py run -h 0.0.0.0