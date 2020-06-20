FROM python:latest

COPY docker_readme.py /
ENTRYPOINT [ "/docker_readme.py" ]

