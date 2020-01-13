#!/usr/bin/python3
""" Takes in a string and sends a search request to the Star Wars API. """
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://swapi.co/api/people/?search={}".
                            format(sys.argv[1]))
    print("Number of results:", response.json().get("count"))
    for result in response.json().get("results"):
        print(result.get("name"))
