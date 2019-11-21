#!/usr/bin/python3
"""
init Rectangle()

allow init with width and height predetermined to 0 on default
width and height values 

"""


class Rectangle:
    """
    class rectangle defined by width and height. 
    """

    def __init__(self, width=0, height=0):
        """
        init
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ gets width"""
        return self.width

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value is not Int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height """
        if type(value) is not Int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ area method of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ method to find perimeter """
        if self.__height is 0 or self.__width is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ string rep """
        detail = ""
        if self.__width is 0 or self.__height is 0:
            return detail
        for x in range(self.__height):
            detail += ("#" * self.__width)
            detail += "\n"
        return detail[:-1]
        
    def __repr__(self):
        """
        prints repr
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        print message when del
        """
        del (self)
        print("Bye rectanlge...")