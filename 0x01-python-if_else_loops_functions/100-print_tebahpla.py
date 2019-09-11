#!/usr/bin/python3
for inc in range(122, 96, -1):
    if inc % 2 != 0:
        print("{:s}".format(chr(inc - 32)), end="")
    else:
        print("{:s}".format(chr(inc)), end="")
