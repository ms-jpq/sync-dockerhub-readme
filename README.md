# Sync Dockerhub Readme

Sync <readme.md> to Dockerhub

## Github Action

```yaml
- name: Sync
  uses: ms-jpq/dockerhub-readme@v1
  with:
    username: <dockerhub username>
    password: <dockerhub password>
    repository: <dockerhub name/repo>
    readme: "./README.md"

```

## Docker Image

```sh

```

