#!/usr/bin/python3
""" square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class """
    def __init__(self, size, x=0, y=0, id=None):
        """ square construct """
        super().__init__(size, size, x, y , id)

    def __str__(self):
        """ string rep """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size)
    
    @property
    def size(self):
        """ gets size """
        return self.width
    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
    
    def to_dictionary(self):
        squaredict = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y         
        }
        return squaredict

    def update(self, *args, **kwargs):

        precheck = len(args)
        if precheck == 0:
            """ set kwargs """
            for key2, value in kwargs.items():
                if key2 == 'id':
                    self.id = value
                elif key2 == 'size':
                    self.size = value
                elif key2 == 'y':
                    self.y = value
                elif key2 == 'x':
                    self.x = value     
            return               
        if precheck == 1:
            self.id = args[0]
            return
        elif precheck == 2:
            self.id = args[0]
            self.size = args[1]
            return
        elif precheck == 3:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            return
        elif precheck == 4:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
            return