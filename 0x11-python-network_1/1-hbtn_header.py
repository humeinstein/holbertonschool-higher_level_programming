#!/usr/bin/python3
""" takes in url and seds request to url and displays value of x request id header """
import sys
import urllib.request


if __name__ == "__main__":
    url = str(sys.argv[1])

    with urllib.request.urlopen(url) as response:
        metainfo = response.info()
        for search in metainfo._headers:
            if "X-Request-Id" in search:
                print(search[1])
