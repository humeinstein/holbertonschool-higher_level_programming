#!/usr/bin/python3
def uppercase(str):
    for upc in str:
        if ord(upc) >= ord('a') and ord(upc) <= ord('z'):
            upc = chr(ord(upc) - 32)
        print("{:s}".format(upc), end="")
    print("")
