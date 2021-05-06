# Docker Data Science 
```bash
cd /path/to/docker-ds
```

# build
```bash
docker build -f Dockerfile -t my-ds-docker .
```

# run
```bash
docker run -p 8888:8888 my-ds-docker
```

# sharing folder between host and docker
```bash
docker run -p 8888:8888 -v /path/to/docker-ds/code:/code my-ds-docker
```

# interactive
```bash
docker container ls --all
docker exec -it containerID /bin/bash
```

# stop
```bash
docker stop containerID
```

# clean
```bash
docker image ls
docker system prune -a
```
