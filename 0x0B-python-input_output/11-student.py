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

    def to_json(self):
        """retrive dict rep"""
        return self.__dict__