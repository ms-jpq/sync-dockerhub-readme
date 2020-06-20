# Sync Dockerhub Readme

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

```sh
docker run -it --rm ms-jpq/sync-dockerhub-readme \
  --username <dockerhub username>\
  --password <dockerhub >\
  --repo <dockerhub name/repo>\
  --readme './README.md'\
```

