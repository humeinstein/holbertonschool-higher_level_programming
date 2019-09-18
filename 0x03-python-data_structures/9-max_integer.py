#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    x = 0
    for o in my_list[::1]:
        if o > x:
            x = o           
    return(x)
        