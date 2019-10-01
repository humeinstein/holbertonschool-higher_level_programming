#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size           
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
    
        ###check if size is int###
        if isinstance(value, int) == False:
            raise TypeError("size must be an integer")
        ###check if size is greater or eq to 0###
        elif value < 0:
            raise ValueError("size must be >= 0")
        ###passed checks so execute###
        else:
            self.__size = value 
    def area(self):
        ###area needs privae __size
        return self.__size * self.__size