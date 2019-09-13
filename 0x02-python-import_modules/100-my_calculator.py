#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    a = sys.argv[1]
    ops = sys.argv[2]
    b = sys.argv[3]

    possibleops = ['+', '-', '*', '/']
    if ops not in possibleops:
        print("Unknown operator. Available operators: +, -, * and / followed wit\
h a new line exit with the value 1")
        exit(1)
    switcher = {
        '+': add(int(a), int(b)),
        '-': sub(int(a), int(b)),
        '*': mul(int(a), int(b)),
        '/': div(int(a), int(b))
        }
    arguments = len(sys.argv)

    if arguments == 4:

        result = switcher.get(ops)
        print("{} {} {} = {}".format(a, ops, b, result))
        exit(0)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
