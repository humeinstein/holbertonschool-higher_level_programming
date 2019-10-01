#!/usr/bin/python3
class Square:
    ##init self size
    def __init__(self, size=0):

        ###check if size is int###
        if isinstance(size, int) == False:
            raise TypeError("size must be an integer")

        ###check if size is greater or eq to 0###
        elif size < 0:
            raise ValueError("size must be >= 0")

        ###passed checks so execute###
        else:
            self.__size = size
            
        ###Init method area###
    def area(self):

        ###area needs privae __size
        self.area = self.__size * self.__size
        return(self.area)