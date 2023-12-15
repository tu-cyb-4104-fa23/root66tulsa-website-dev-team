# Deployment Instructions

1. **Install Docker and Docker Compose**
    - Docker is required to build and run the Docker image. 
    - Docker Compose is required to run the Docker image. 
    - Docker Compose is included with [Docker Desktop](https://www.docker.com/products/docker-desktop/) for Windows and Mac. 
        - For Linux, follow the instructions [[here]([www.google.com](https://linuxhandbook.com/docker-compose-quick-start/))].

2. **Clone the project**
   - `git clone <repository_url>`

3. **Navigate to the project directory**
   - `cd <project_directory>`

4. **Build the Docker image**
    - `docker compose up --build`
    - Rebuild the image using this command if changes are made to the project. 
    - The initial build may take some time, but subsequent builds will be much faster
    - After the initial build, the project can be run with `docker compose up` 
  
For more information on Docker and Docker Compose, see the [Docker documentation](https://docs.docker.com/).

## Setting Environment Variables

1. **Create a `.env` file** in the project root directory
2. **Set environment variables in the format** `VARIABLE_NAME=value`
3. **Reference environment variables in `docker-compose.yml`**
   1. see `docker-compose.yml` for examples