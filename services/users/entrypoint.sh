#!/bin/sh

echo "Waiting for Postgres init..."

while ! nc -z users-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started on port 5432"

python manage.py run -h 0.0.0.0