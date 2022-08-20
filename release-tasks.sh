#!/bin/bash

python manage.py migrate --noinput --settings django_src.settings.heroku
echo "READY"
