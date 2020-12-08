#!/usr/bin/python3
def remove_char_at(str, n):
    string1 = ""
    for num1 in range(0, len(str)):
        if num1 != n:
            string1 += str[num1]
    return string1
