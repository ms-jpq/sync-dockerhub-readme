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

Optionally, you can replace strings in your readme file. For example, to avoid broken images, you can exchange relative image URLs like `![MyImage](./doc/image.svg)` with absolute URLs like `![MyImage](https://github.com/myuser/myrepo/raw/main/doc/image.svg))`:

```yaml
- name: Sync
  uses: ms-jpq/sync-dockerhub-readme@v1
  with:
    username: <dockerhub username>
    password: <dockerhub password>
    repository: <dockerhub name/repo>
    readme: "./README.md"
    replace_pattern: "](./"
    replace_with: "](${{ github.server_url }}/${{ github.repository }}/raw/${{ github.ref_name }}/"
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

