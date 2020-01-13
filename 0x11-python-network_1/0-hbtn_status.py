#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    print("Body response:")
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as request:
        response = request.read()
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode("utf-8")))
