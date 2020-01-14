#!/usr/bin/python3
""" Takes in a string and sends a search request to the Star Wars API. """
import requests
import sys


if __name__ == "__main__":
    requested = {}
    response = requests.get("https://swapi.co/api/people/?search={}".
                            format(sys.argv[1]))
    print("Number of results:", response.json().get("count"))
    while True:
        for result in response.json().get("results"):
            print(result.get("name"))
            for film in result.get("films"):
                if film in requested.keys():
                    film_title = requested[film]
                else:
                    film_title = requests.get(film).json()["title"]
                    requested[film] = film_title
                print("\t{}".format(film_title))
        next_page = response.json().get("next")
        if not next_page:
            break
        response = requests.get(next_page)
