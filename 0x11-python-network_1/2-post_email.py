#!/usr/bin/python3
""" takes in url and email and seds a post request to url with email as parameter """
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    emaildata = {'email' : email}
    emaildata = urllib.parse.urlencode(emaildata)
    emaildata = emaildata.encode('ascii')
    with urllib.request.urlopen(url, emaildata) as response:
        print(response.read().decode('utf-8'))
