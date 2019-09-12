#!/usr/bin/python3
import sys


print("This is the name of the script %s" % (sys.argv[0]))

print("The arguments are : %s" % str(sys.argv))



arguments = len(sys.argv)
if arguments == 0:
    print("{:d} arguments:".format(arguments - 1))
else:
    print("{:d} arguments.".format(arguments - 1))

x = 1
while x != arguments:
    print("{:d}: %s".format(x) % str(sys.argv[x]))
    x = x + 1
