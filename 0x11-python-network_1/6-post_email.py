#!/usr/bin/python3
""" email post """

if __name__ == "__main__":
    import requests
    import sys


    emailer = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], emailer)
    print(response.text)
