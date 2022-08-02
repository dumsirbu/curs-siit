#!/bin/bash
python manage.py migrate
python manage.py createsuperuser --noinput --username admin1
case $1 in
    local-server)
        python manage.py runserver 0.0.0.0:8000
    ;;
    production-server)
        uwsgi --http :8000 --wsgi-file siit/wsgi.py 
    ;;
    *)
        $1
    ;;
esac