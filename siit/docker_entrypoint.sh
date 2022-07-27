#!/bin/bash
python manage.py migrate
python manage.py createsuperuser --noinput --username admin1
#python manage.py runserver 0.0.0.0:8000
uwsgi --http :8000 --wsgi-file siit/wsgi.py 