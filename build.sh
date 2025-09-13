#!/usr/bin/env bash
cd social_media_api &&  set -o errexit

cd social_media_api && pip install -r requirements.txt

cd social_media_api &&  python manage.py collectstatic --no-input

cd social_media_api &&  python manage.py migrate accounts

cd social_media_api &&  python manage.py migrate --no-input
