#!/usr/bin/python3

for x in range(0, 8):
    for xx in range(x, 10):
        if x != xx:
            print("{:d}{:d}".format(x, xx), end=", ")
print(89)
