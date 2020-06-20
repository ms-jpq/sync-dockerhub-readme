# [Sync Dockerhub Readme](https://ms-jpq.github.io/sync-dockerhub-readme)

Sync <readme.md> to Dockerhub

## Github Action

```yaml
- name: Sync
  uses: ms-jpq/sync-dockerhub-readme@v1
  with:
    username: <dockerhub username>
    password: <dockerhub password>
    repository: <dockerhub name/repo>
    readme: "./README.md"

```

## Docker Image

[![Docker Pulls](https://img.shields.io/docker/pulls/msjpq/sync-dockerhub-readme.svg)](https://hub.docker.com/r/msjpq/sync-dockerhub-readme/)

```sh
docker run -it --rm msjpq/sync-dockerhub-readme \
  --username <dockerhub username> \
  --password <dockerhub password> \
  --repo <dockerhub name/repo> \
  --readme './README.md'
```

