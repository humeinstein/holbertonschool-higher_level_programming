#!/usr/bin/python3
"""
function that prints a square with the character #
"""
def print_square(size):
    """
    returns size * #
    """
    wow = checkStatus(size)
    if wow == 0:
        for i in range(size):
            print("#" * size)
    elif wow == 1:
        raise TypeError("size must be an integer")
    else:
        raise TypeError("size must be >= 0")
"""
function that checks status to return
"""
def checkStatus(size):
    """
    returns status for print_square
    """
    status = 0
    if type(size) is not int:
        status = 1
    if size < 0:
        if type(size) is float:
            status = 1
        status = 2
    return status
