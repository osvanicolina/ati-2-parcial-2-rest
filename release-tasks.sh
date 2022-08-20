#!/bin/bash

python manage.py migrate --noinput --settings django_src.settings.heroku
python manage.py loaddata fixtures/admin.json
