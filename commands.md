


Build docker Image: `docker build -t health-service-app .`

Run docker container `docker run -d -p 8000:8000 --name health-service-app health-service-app`

Stop running Container - `docker stop health-service-app` ✅

Start stopped Container - `docker start health-service-app`

Restart container - `docker restart health-service-app`

Remove Docker Container - `docker rm health-service-app` ✅ 

Remove Docker Image: `docker rmi health-service-app`

view running container - `docker ps`

view all container - `docker ps -a`

view docker images `docker images`


logs:
    docker logs -f <container_name_or_id>
    docker logs -f health-service-app


docker login --username <githhub-user-name> --password <your_password> ghcr.io

docker login --username chinmayjaiswal --password {{ secrets.GHCR_PAT }} ghcr.io

docker build . -t ghcr.io/<USERNAME>/<IMAGE_NAME>:<TAG>

`docker build . -t ghcr.io/chinmayjaiswal/health-service-app:sha12345`

docker push ghcr.io/<USERNAME>/<IMAGE_NAME>:<TAG>

`docker push ghcr.io/chinmayjaiswal/health-service-app:sha12345`




