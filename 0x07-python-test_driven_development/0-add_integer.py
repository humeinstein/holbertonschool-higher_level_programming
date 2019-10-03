#!/usr/bin/python3
"""

func that adds 2 ints/floats together

"""
def add_integer(a, b=98):
    """
        return sum
    """
    if not(type(a) is int or type(a) is float):
        raise TypeError("a must be an integer")
    if not(type(b) is int or type(b) is float):
        raise TypeError("b must be an integer")

    sumof = int(a) + int(b)
    return sumof
