#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lastdigit = str(number)
if int(lastdigit[-1]) > 5:
    thenthus = " and is greater than 5"
elif int(lastdigit[-1]) == 0:
    thenthus = " and is 0"
elif int(lastdigit[-1]) != 0 & int(lastdigit[-1]) < 6:
    thenthus = " and is less than 6 and not 0"
else:
    pass
lastdigits = "Last digit of " + str(number) + " is " + lastdigit[-1] + thenthus

print(lastdigits)
