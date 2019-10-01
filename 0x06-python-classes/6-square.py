#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position       
    ###size.setter
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
    ###position.setter
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        ##check type of value
        if type(value) != tuple or value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        ###area needs privae __size
        return self.__size * self.__size
    
    def my_print(self):
        ###check if __position1
        for x in range(0, self.__position[1]):
            print()
        for x in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(end="_")
            for x in range(0, self.__size):
                print("#".format(), end="")   
            print("#")
        if self.__size == 0:
            print()
    
    