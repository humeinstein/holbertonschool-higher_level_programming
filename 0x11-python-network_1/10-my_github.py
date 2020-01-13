#!/usr/bin/python3
""" takes username and password and displays id w/ghAPI """

import sys
import requests


if __name__ == '__main__':

 
    json = requests.get("https://api.github.com/user", auth=(sys.argv[1], sys.argv[2])).json()


    try:
        print(json["id"])
    except:
        print(None)
