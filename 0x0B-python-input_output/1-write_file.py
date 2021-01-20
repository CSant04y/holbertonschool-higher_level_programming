#!/usr/bin/python3
"""function that writes a string to a text file (UTF8) and
    returns the number of characters written:
"""


def write_file(filename="", text=""):
    """This writes to text file and overwrites it if it already exists

    Args:
        filename (str, optional): [The name of the file]. Defaults to "".
        text (str, optional): [The text to be placed in file]. Defaults to "".
    """
    count = 0
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)
