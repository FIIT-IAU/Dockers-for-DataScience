# Docker Data Science /home/user/work/docker/ds

# build
docker build -f Dockerfile -t ds-docker .
	
# run
docker run -p 8888:8888 ds-docker
	
# sharing folder between host and docker
docker run -p 8888:8888 -v /home/user/work/docker/ds/code:/code ds-docker
	
# interactive
docker container ls --all
docker exec -it containerID /bin/bash
	
# stop
docker stop containerID
	
# clean
docker image ls
docker system prune -a
