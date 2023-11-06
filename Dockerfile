#!/bin/bash
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./root66_website /app/
# CMD python /app/manage.py runserver 0.0.0.0:8000