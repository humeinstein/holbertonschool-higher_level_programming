#!/usr/bin/python3
"""
function that checks status of str
returns status
"""
def checkStatus(first_name, last_name):
    """
    return status of 0 if all str. 1 | 2 for first or last
    """
    status = 0
    if type(first_name) is not str:
        status = 1
    if type(last_name) is not str:
        status = 2
    return status

"""
function that print " My name is <first name> <last name>
"""
def say_my_name(first_name, last_name=""):
    """
    containts checkStatus and returns full name or error
    """
    status = checkStatus(first_name, last_name)
    if status is 0:
        print("My name is {} {}".format(first_name, last_name)) 
    elif status is 1:
        status = "first_name"
        raise TypeError("{} must be a string".format(status))
    else:
        status = "last_name"
        raise TypeError("{} must be a string".format(status))
