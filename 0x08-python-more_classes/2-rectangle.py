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
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) == False:                        
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) == False:                        
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    """
    returns area of h w
    """
    def area(self):
        """
        gets area
        """
        return self.__height * self.__width
    def perimeter(self):
        return (self.__height * 2) + (self.__width * 2)