#!/usr/bin/python3
""" Lists 10 commits (from the most recent to oldest) of a repository. """
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://api.github.com/repos/{}/{}/commits".
                            format(sys.argv[2], sys.argv[1]),
                            params={"per_page": 10})
    for commit in response.json():
        print("{}: {}".format(commit.get("sha"), commit.get("commit").
                              get("author").get("name")))
