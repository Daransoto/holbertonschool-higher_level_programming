#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    print("Body response:")
    response = requests.get("https://intranet.hbtn.io/status")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
