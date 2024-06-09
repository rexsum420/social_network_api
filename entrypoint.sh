#!/bin/sh
set -e
echo "Apply database migrations"
python manage.py migrate

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Starting server"
exec "$@"
