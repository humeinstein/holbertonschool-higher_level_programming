#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)
    elif idx > len(my_list) - 1:
        return(my_list)
    else:
        for x, i in enumerate(my_list):
            if i == idx:
                my_list[i] = element
        return(my_list) 