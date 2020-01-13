#!/usr/bin/python3
""" search starwars using api """

import requests
import sys

if __name__ == '__main__':
    json = requests.get("https://swapi.co/api/people/?search={}".format(
        sys.argv[1])).json()
    print("Number of results: {}".format(len(json["results"])))
    for name in json["results"]:
        print(name["name"])
