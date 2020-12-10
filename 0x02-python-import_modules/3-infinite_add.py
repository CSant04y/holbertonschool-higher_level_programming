#!/usr/bin/python3
import sys

length = len(sys.argv)
num1 = 0

for i in range(1, length):
    num1 += int(sys.argv[i])
print("{:d}".format(num1))
