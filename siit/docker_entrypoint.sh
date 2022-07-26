#!/bin/bash
python manage.py migrate
python manage.py createsuperuser --noinput --username admin1
python manage.py runserver 0.0.0.0:8000