#!/usr/bin/python3
"""
rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """ class construct """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get width """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ sets width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get height """
        return(self.__height)

    @height.setter
    def height(self, value):
        """ sets height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ gets x """
        return(self.__x)

    @x.setter
    def x(self, value):
        """ sets x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ gets y """
        return(self.__y)
    @y.setter
    def y(self, value):
        """ sets y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value

    def area(self):
        """ area """
        area = self.height * self.width
        if area <= 0:
            raise ValueError("area is not existent")
        else:
            return area

    def display(self):
        """ print # y is nline x is whitespace """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)
        detail = ""
    
    def __str__(self):
        """print string rep"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height)
    
    def to_dictionary(self):
        rectangledict = { 
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width          
        }
        return rectangledict

    def update(self, *args, **kwargs):
        """ update rectangle """
        precheck = len(args)
        if precheck == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
            return
        if precheck == 1:
            self.id = args[0]
            return
        elif precheck == 2:
            self.id = args[0]
            self.__width = args[1]
            return
        elif precheck == 3:
            self.id = args[0]
            self.__width = args[2]
            self.__height = args[3]
            return
        elif precheck == 4:
            self.id = args[0]
            self.__width = args[2]
            self.__height = args[3]
            self.__x = args[3]
            return
        else:
            self.id = args[0]
            self.__width = args[2]
            self.__height = args[3]
            self.__x = args[3]
            self.__y = args[4]
            return
    