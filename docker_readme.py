#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace
from json import dumps, loads
from os import environ
from shutil import get_terminal_size
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
    parser.add_argument("--username", required=not username, default=username)

    password = environ.get("DOCKER_PASSWORD")
    parser.add_argument("--password", required=not password, default=password)

    parser.add_argument("--readme", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--replace-pattern", type=str, required=False)
    parser.add_argument("--replace-with", type=str, required=False)

    args = parser.parse_args()
    return args


def login(username: str, password: str) -> str:
    uri = "https://hub.docker.com/v2/users/login/"
    data = {"username": username, "password": password}
    req = Request(
        uri,
        method="POST",
        headers={"Content-Type": "application/json"},
        data=dumps(data).encode(),
    )
    with urlopen(req) as resp:
        msg = resp.read().decode()
        return loads(msg)["token"]


def set_repo(token: str, repo: str, readme: str) -> str:
    uri = f"https://hub.docker.com/v2/repositories/{repo}/"
    data = {"full_description": readme}
    req = Request(
        uri,
        method="PATCH",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        data=dumps(data).encode(),
    )
    with urlopen(req) as resp:
        msg = resp.read().decode()
        return loads(msg)["full_description"]


def replace_patterns(readme: str, replace_pattern: str, replace_with: str) -> str:
    return readme.replace(replace_pattern, replace_with)


def main() -> None:
    args = parse_args()
    print(args)
    readme = slurp(args.readme)
    if args.replace_pattern and args.replace_with:
        readme = replace_patterns(readme, args.replace_pattern, args.replace_with)
    token = login(args.username, args.password)
    desc = set_repo(token=token, repo=args.repo, readme=readme,)
    big_print(desc)


main()
