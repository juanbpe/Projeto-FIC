#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate


# Criação de super usuário
DJANGO_SUPERUSER_PASSWORD=1234@Ifrn
python manage.py createsuperuser --username admin