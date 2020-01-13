#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays the body of the
    response (decoded in utf-8). """
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as request:
            response = request.read()
        print(response.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
