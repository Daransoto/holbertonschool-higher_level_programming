#!/usr/bin/python3
""" Lists 10 commits (from the most recent to oldest) of a repository. """
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://api.github.com/repos/{}/{}/commits".
                            format(sys.argv[2], sys.argv[1]))
    for i in range(10):
        print("{}: {}".format(response.json()[i].get("sha"), response.
                              json()[i].get("commit").get("author").
                              get("name")))
