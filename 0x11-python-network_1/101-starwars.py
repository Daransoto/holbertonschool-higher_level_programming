#!/usr/bin/python3
""" Takes in a string and sends a search request to the Star Wars API. """
import requests
import sys


if __name__ == "__main__":
    response = requests.get("https://swapi.co/api/people/?search={}".
                            format(sys.argv[1]))
    print("Number of results:", response.json().get("count"))
    while True:
        for result in response.json().get("results"):
            print(result.get("name"))
        next_page = response.json().get("next")
        if not next_page:
            break
        response = requests.get(next_page)
