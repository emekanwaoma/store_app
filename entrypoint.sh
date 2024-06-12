#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/

/opt/venv/bin/python manage.py migrate

if [ "$DEBUG" = "0" ]; then
    /opt/venv/bin/python manage.py collectstatic --noinput
    /opt/venv/bin/gunicorn \
            --access-logfile - \
            --worker-class=gevent \
            --worker-connections=100 \
            --timeout 9900 \
            --workers 3 \
            --bind unix:/home/store/store.sock \
            store.wsgi:application
else
    /opt/venv/bin/python manage.py runserver "0.0.0.0:${APP_PORT}"

fi