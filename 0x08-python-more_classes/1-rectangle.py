#!/usr/bin/python3
"""
init Rectangle()

allow init with width and height predetermined to 0 on default
width and height values 

"""
class Rectangle():
    """
    class rectangle defined by width and height. 
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        self.width = width
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        elif type(value) is not int:                        
            raise TypeError("width must be an integer")
        else:
            self.__width = value
    @property
    def height(self):
        self.height = height
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        elif type(value) is not int:                        
            raise TypeError("height must be an integer")
        else:
            self.__height = value