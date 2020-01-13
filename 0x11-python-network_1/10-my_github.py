#!/usr/bin/python3
""" Takes your Github credentials (username and password) and uses the Github
    API to display your id. """
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    if "id" in response.json():
        print(response.json().get("id"))
    else:
        print("None")
