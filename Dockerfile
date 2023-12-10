# Base image
FROM python:3.9-slim-buster

# Setup environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV AppDir=/app

# Create a non-root user with a home directory
RUN useradd -m appuser

# Create app directory & give ownership to the non-root user
RUN mkdir -p $AppDir && \
    chown -R appuser:appuser $AppDir

# Where your code lives
WORKDIR $AppDir

# Switch to non-root user
USER appuser

# Install dependencies
COPY --chown=appuser:appuser requirements.txt $AppDir

# Install dependencies globally as root
USER root
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Switch back to non-root user
USER appuser

# Copy whole project to your docker home directory.
COPY --chown=appuser:appuser ./root66_website $AppDir

# Port where the Django app runs
EXPOSE 8000
