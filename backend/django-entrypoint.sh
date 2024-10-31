#!/bin/bash

sleep 5

echo "=============================="
echo "Create Migrations"
python manage.py makemigrations

echo "=============================="
echo "Apply Migrations"
python manage.py migrate

echo "Starting Django Server..."
python manage.py runserver 0.0.0.0:8000