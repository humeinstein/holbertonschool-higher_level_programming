#!/usr/bin/python3
"""
create subclassclass
"""
class MyList(list):
    """subclass"""
    def __init__(self):
        """init"""
        super().__init__()

    def print_sorted(self):
        """print sorted"""
        print(sorted(self))