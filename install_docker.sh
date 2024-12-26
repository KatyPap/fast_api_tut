#!/bin/bash

#to install docker 
#1) make the file executable with:  chmod +x install_docker.sh
#2) run the file: ./install_docker.sh

curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

curl -fsSL https://test.docker.com -o test-docker.sh
sh test-docker.sh

git clone https://github.com/docker/docker-ce.git
cd docker-ce
sh install.sh

#verify docker installation 
docker --version

#start docker
dockerd &