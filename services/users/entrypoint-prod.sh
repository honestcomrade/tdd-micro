#!/bin/sh

echo "Waiting for Postgres init..."

# netcat will send empty traffic to the users-db host
# while that is not able to connect, sleep and try again
# then finish
while ! nc -z users-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# now that we have made connection with the pg db
# we can run the manage script
gunicorn -b 0.0.0.0:5000 manage:app