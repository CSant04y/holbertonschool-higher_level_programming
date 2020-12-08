#!/usr/bin/python3
for num1 in range(122, 96, -1):
    if num1 % 2 == 0:
        print("{:c}".format(num1), end='')

    else:
        print("{:c}".format(num1 - 32), end='')
