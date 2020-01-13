#!/usr/bin/python3
""" fetches url using urllib """
import urllib.request

url = "https://intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    content = response.read()
    typeof = type(content)
    utfcontent = content.decode('utf-8')

    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
        typeof, content, utfcontent))
