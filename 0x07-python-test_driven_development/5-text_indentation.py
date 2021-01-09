#!/usr/bin/python3
"""print text with 2 newlines after '.' '?' or ':' in string"""


def text_indentation(text):
    """prints text with 2 newlines after '.' '?' or ':' chars"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    prev = ""
    for i in text:
        if i is " " and i is text[0] and prev is "":
            prev = "\n"
            continue

        if i is " " and prev is "\n":
            continue

        if i is "." or i is "?" or i is ":":
            print(i)
            print()
            prev = "\n"

        else:
            print(i, end="")
            prev = i
