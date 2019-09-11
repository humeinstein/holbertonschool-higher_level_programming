#!/usr/bin/python3
def fizzbuzz():
    for inc in range(1, 101):
        if inc % 5 == 0 and inc % 3 == 0:
            print("FizzBuzz ", end="")
        elif inc % 3 == 0:
            print("Fizz ", end="")
        elif inc % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(inc), end="")
