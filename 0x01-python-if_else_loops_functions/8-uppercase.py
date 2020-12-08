#!/usr/bin/python3
def uppercase(str):
    newstr = ''
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            newstr += chr(ord(letter) - 32)
        else:
            newstr += letter

    print("{}".format(newstr))
