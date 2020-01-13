#!/usr/bin/python3
""" Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter. """
import requests
import sys


value = {"q": ""}
if len(sys.argv) > 1:
    value["q"] = sys.argv[1]
response = requests.post("http://0b77dee8aa88.19.hbtn-cod.io:5000/search_user",
                         data=value)
try:
    if response.json() in ["", {}, None]:
        print("No result")
    else:
        print("[{}] {}".format(response.json()["id"], response.json()["name"]))
except ValueError:
    print("Not a valid JSON")
