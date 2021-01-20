#!/usr/bin/python3
"""function that appends a string at the end of a text file
 (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """This appends string at end of txt file

    Args:
        filename (str, optional): [name of file]. Defaults to "".
        text (str, optional): [string to be appended]. Defaults to "".
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
