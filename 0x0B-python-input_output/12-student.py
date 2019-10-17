#!/usr/bin/python3
"""
class student
"""

class Student:
    """dfine"""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrive dict rep"""
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for att in attrs:
            if type(att) is not str:
                return self.__dict__
        return {x: self.__dict__[x] for x in self.__dict__ if x in attrs}