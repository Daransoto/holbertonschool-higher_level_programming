#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter. """
import requests
import sys


value = {"q": ""}
if len(sys.argv) > 1:
    value["q"] = sys.argv[1]
response = requests.post("http://0.0.0.0:5000/search_user", data=value)
try:
    if not response or response.json() in ["", {}, None]:
        print("No result")
    else if "id" not in response.json().keys() or "name" not in \
       response.json().keys():
        raise ValueError
    else:
        print("[{}] {}".format(response.json().get("id"),
                               response.json().get("name")))
except ValueError:
    print("Not a valid JSON")
