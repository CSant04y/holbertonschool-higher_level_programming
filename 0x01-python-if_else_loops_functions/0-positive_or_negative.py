#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#check to see if a number is neg or postive using if statment
if number < 0:
    print('{} is negative'.format(number))
elif number > 0:
    print('{} is postive'.format(number))
else:
    print('{} is zero'.format(number))
