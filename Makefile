docker restart:
	sudo docker-compose -f docker-compose-dev.yml down
	sudo docker-compose -f docker-compose-dev.yml up -d --build
docker down:
	sudo docker-compose -f docker-compose-dev.yml down