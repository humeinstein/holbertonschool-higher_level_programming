#!/usr/bin/python3

class MyInt(int):
    """define class"""

    def __eq__(self, other):
        """ change to !="""
        return int.__ne__(self, other)


    def __ne__(self, other):
        """ change to == """
        return int.__eq__(self, other)