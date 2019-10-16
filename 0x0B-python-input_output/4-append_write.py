#!/usr/bin/python3
"""
append
"""


def append_write(filename="", text=""):
    """appends string"""
    with open(filename, mode='a', encoding='utf-8') as filec:
        return filec.write(text)