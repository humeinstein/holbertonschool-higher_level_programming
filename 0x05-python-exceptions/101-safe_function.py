#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *arhs):
    try:
        result = fct(*args)
    except Exception as sf:
        stderr.write("Exception: {}\n".format(sf))
        return None
    return result

