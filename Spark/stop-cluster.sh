#!/bin/bash

echo " ---- WARNING ---- "
echo "This will stop or remove all the containers on the host"
echo "Do you want to stop or remove? stop/remove"

read userInput

if [ $userInput = "stop" ]; then 
	docker stop $(docker ps -a -q) 
elif [ $userInput = "remove" ]; then
	docker-compose -f docker-compose-cluster.yml down -v
else
	echo "Invalid input. Please enter 'stop' or 'remove'."
fi