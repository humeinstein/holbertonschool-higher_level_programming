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
        """
        define width on self
        """
        return self.width
    @width.setter
    def width(self, value):
        """
        setter of width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        """
        define height
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        set height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer\n")
        elif value < 0:
            raise TypeError("height must be >= 0\n")
        else:
            self.__height = value