#!/usr/bin/python3
"""
reads n lines of text file
"""


def read_lines(filename="", nb_lines=0):
    """read n lines"""
    x = 0
    with open(filename, encoding='utf-8') as filec:
        if nb_lines <= 0:
            print(filec.read(), end='')
        for i, l in enumerate(filec):
            x = i
            if x < nb_lines:
                print(l, end="")

            