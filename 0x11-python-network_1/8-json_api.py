#!/usr/bin/python3
""" takes in letter and sends post request with letter """
import requests
from requests import post
import sys


if __name__ == '__main__':

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    try:
        response = post("http://0.0.0.0:5000/search_user", {'q': q}).json()
        if "id" in response and "name" in response:
            print("[{}] {}".format(response["id"], response["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
