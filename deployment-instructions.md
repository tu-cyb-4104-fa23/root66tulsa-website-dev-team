# Deployment Instructions

Build docker image: `docker build -t root66-site .`

Create and run container:

`docker run -dp 9000:9000 root66-test python /app/manage.py runserver 0.0.0.0:9000`

Verify server has started by visiting `localhost:9000` on browser