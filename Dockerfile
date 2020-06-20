FROM python:alpine

COPY docker_readme.py /
ENTRYPOINT [ "/docker_readme.py" ]

