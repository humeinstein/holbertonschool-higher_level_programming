#!/usr/bin/python3
"""
BG class
"""

class BaseGeometry:
    """get area"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """rectangle class sub of Base"""
    def __init__(self, width, height):
        """instant with width and height"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__width * self.__height
    def __str__(self):
        """string rep"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

class Square(Rectangle):
    """square class inherit Rect -> Geoclass"""
    def __init__(self, size):
        """instantize"""
        self.__size = size
        super().__init__(self.__size, self.__size)
    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)