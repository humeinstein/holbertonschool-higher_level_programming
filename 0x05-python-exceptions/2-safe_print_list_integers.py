#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    realindex = 0
    try:
        while index < x:
            if isinstance(my_list[index], int) == True:
                print("{}".format(my_list[index]), end="")
                realindex += 1
            index += 1
        print()
    except (ValueError, TypeError):
        pass
    return(realindex)
