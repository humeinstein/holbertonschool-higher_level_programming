#!/usr/bin/python3
"""
readfile&print
"""

def read_file(filename=""):
    """read file"""
    with open(filename, 'r', encoding='utf-8') as filec:
        print(filec.read() end="")
