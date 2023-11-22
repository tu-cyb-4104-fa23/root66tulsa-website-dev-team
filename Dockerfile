# Base image
FROM python:3

# Setup environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV AppDir=/app

# Set work directory
RUN mkdir -p $AppDir

# Where your code lives
WORKDIR $AppDir

# Install dependencies
COPY requirements.txt $AppDir
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy whole project to your docker home directory.
COPY ./root66_website $AppDir

# Copy entrypoint.sh
COPY ./entrypoint.sh $AppDir

# Port where the Django app runs
EXPOSE 8000
