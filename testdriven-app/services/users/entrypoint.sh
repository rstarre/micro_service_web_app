#!/bin/sh

echo "waiting for postgres...."

while ! nc -z users_db 5432; do
    sleep 0.1
    echo "not started yet"
done

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0