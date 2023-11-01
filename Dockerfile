# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /root66_website
COPY requirements.txt /root66_website/
RUN pip install -r requirements.txt
COPY . /root66_website/