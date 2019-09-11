#!/usr/bin/python3

def print_last_digit(number):
    lastdigit = number % 10
    if lastdigit < 0:
        lastdigit = lastdigit * -1
    print("{:d}".format(lastdigit), end="")
    return lastdigit
