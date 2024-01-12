#!/bin/bash

# Stop on the first sign of trouble
set -e

# The name of the docker image
IMAGE_NAME="web-scraper-app"

echo "Starting deployment process..."

# Check for any running containers of the same image and stop them
echo "Checking for existing containers..."
if [ $(docker ps -q -f name=$IMAGE_NAME | wc -l) -gt 0 ]; then
    echo "Stopping running containers..."
    docker stop $(docker ps -q -f name=$IMAGE_NAME)
fi

# Remove stopped containers of the same image
if [ $(docker ps -aq -f status=exited -f name=$IMAGE_NAME | wc -l) -gt 0 ]; then
    echo "Removing stopped containers..."
    docker rm $(docker ps -aq -f status=exited -f name=$IMAGE_NAME)
fi

# Build the docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Run the newly built image
echo "Running Docker image..."
docker run -d --name $IMAGE_NAME -p 80:80 $IMAGE_NAME

echo "Deployment completed successfully."