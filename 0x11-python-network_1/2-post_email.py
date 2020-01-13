#!/usr/bin/python3
""" Takes in a URL and an email, sends a POST request to the passed URL with
    the email as a parameter, and displays the body of the response """
import urllib.request
import sys


if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as request:
        response = request.read()
    print(response.decode("utf-8"))
