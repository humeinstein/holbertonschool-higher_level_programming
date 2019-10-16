#!/usr/bin/python3
"""
readfile&print
"""
def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as filec:
        for i, l in enumerate(filec):
            pass
    return i + 1