#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = len(sys.argv)

    x = 1
    sumof = 0
    while x != arguments:
        sumof = sumof + int(sys.argv[x])
        x = x + 1
    print(sumof)
