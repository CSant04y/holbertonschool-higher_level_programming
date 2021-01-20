#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Function reads from textfile and prints to STDOUT

    Args:
        filename (str, optional): [The name of the file]. Defaults to "".
    """
    with open(filename) as f:
        print(f.read())
