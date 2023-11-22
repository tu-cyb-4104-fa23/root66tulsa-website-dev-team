#!/bin/bash

# Make migrations (comment out if not needed)
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver 0.0.0.0:8000 --insecure