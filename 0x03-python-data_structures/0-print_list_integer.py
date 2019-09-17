#!/usr/bin/python3
def print_list_integer(my_list=[]):
    total = len(my_list)
    inct = 0

    for inct in range(0, total):
        print("{:d}".format(my_list[inct]))
