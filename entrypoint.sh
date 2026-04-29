#!/bin/sh

set -e

python manage.py migrate --noinput

if [ "$DEBUG" = "True" ] || [ "$DEBUG" = "true" ] || [ "$DEBUG" = "1" ]; then
    exec python manage.py runserver 0.0.0.0:${PORT:-8000}
fi

python manage.py collectstatic --noinput
exec gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3