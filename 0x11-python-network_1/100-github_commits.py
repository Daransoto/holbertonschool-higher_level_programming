#!/usr/bin/python3
""" Lists 10 commits (from the most recent to oldest) of a repository. """
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://api.github.com/repos/{}/{}/commits".
                            format(sys.argv[1], sys.argv[2]))
    for i in range(10):
        print("{}: {}".format(response.json()[i]["sha"], response.
                              json()[i]["commit"]["author"]["name"]))
