#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace
from json import dumps, loads
from os import environ
from shutil import get_terminal_size
from sys import stderr
from typing import Any
from urllib.request import Request, urlopen


def big_print(msg: str) -> None:
  _, cols = get_terminal_size()
  print(cols * "-")
  print(msg)
  print(cols * "-")


def slurp(path: str) -> str:
  with open(path) as fd:
    return fd.read()


def parse_args() -> Namespace:
  parser = ArgumentParser()

  username = environ.get("DOCKER_USERNAME")
  parser.add_argument("--username",
                      required=not username,
                      default=username)

  password = environ.get("DOCKER_PASSWORD")
  parser.add_argument("--password",
                      required=not password,
                      default=password)

  parser.add_argument("--readme", required=True)
  parser.add_argument("--repos", required=True, nargs="+")

  args = parser.parse_args()
  return args


def login(username: str, password: str) -> str:
  uri = f"https://hub.docker.com/v2/users/login/"
  data = {"username": username, "password": password}
  req = Request(
      uri,
      method="POST",
      headers={"Content-Type": "application/json"},
      data=dumps(data).encode())
  with urlopen(req) as resp:
    msg = resp.read().decode()
    return loads(msg)["token"]


def set_repo(token: str, repo: str, readme: str) -> str:
  uri = f"https://hub.docker.com/v2/repositories/{repo}/"
  data = {"full_description": readme}
  req = Request(
      uri,
      method="PATCH",
      headers={"Content-Type": "application/json",
               "Authorization": f"Bearer {token}"},
      data=dumps(data).encode())
  with urlopen(req) as resp:
    msg = resp.read().decode()
    return loads(msg)["full_description"]


def main() -> None:
  args = parse_args()
  readme = slurp(args.readme)
  token = login(args.username, args.password)
  for repo in args.repos:
    desc = set_repo(
        token=token,
        repo=repo,
        readme=readme,
    )
    big_print(repo)
    print(desc)


main()

