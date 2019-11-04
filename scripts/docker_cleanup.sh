#!/usr/bin/env bash

clean_containers() {
    containers=$(docker ps -q)
    echo "Stopping any running containers..."
    docker stop $containers
    echo "Removing all containers..."
    docker rm -v $containers 2>/dev/null
    echo "Containers removed from system."
}

clean_images() {
    echo "Removing Docker images..."
    docker rmi --force $(docker images -q 2>/dev/null) 2>/dev/null
    echo "All Docker images removed from system."
}

clean_environments() {
    echo "Removing leftover volumes..."
    docker volume rm --force $(docker volume ls -q)
    echo "Pruning leftover networks..."
    docker network prune --force
}

echo "Cleaning up Docker environment..."
clean_containers
clean_images
clean_environments
echo "Done."
