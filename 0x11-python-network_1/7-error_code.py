#!/usr/bin/python3
""" print request error codes """

import requests
import sys


if __name__ == '__main__':

    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)

    except:
        print("Error code: {}".format(response.status_code))
