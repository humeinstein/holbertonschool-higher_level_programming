#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for hee in matrix:
        inc = 0
        for heehee in hee:
            if inc == len(hee) - 1:
                print("{:d}".format(heehee), end ="")
            else:
                print("{:d}".format(heehee), end=" ")
            inc = inc + 1
        print()    