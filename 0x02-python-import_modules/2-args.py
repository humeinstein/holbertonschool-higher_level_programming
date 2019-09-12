#!/usr/bin/python3
import sys

arguments = len(sys.argv)
if arguments == 1:
    print("{:d} arguments.".format(arguments - 1))
elif arguments == 2:
    print("{:d} argument:".format(arguments - 1))
else:
    print("{:d} arguments:".format(arguments - 1))

x = 1
while x != arguments:
    print("{:d}: %s".format(x) % str(sys.argv[x]))
    x = x + 1
