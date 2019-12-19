#!/usr/bin/python3
"""class recge
"""


class Rectangle:
    """creates base height and width of the rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Institation of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """gets the area"""
        return self.width * self.height

    def perimeter(self):
        """gets the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """return string of rect"""
        if self.width == 0 or self.height == 0:
            return ""
        result = str(self.print_symbol) * self.width
        return '\n'.join(list(result for i in range(self.height)))

    def __repr__(self):
        """return string rep"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """delete the square"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
