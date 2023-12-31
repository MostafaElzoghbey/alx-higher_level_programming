#!/usr/bin/python3

"""Function that reads a text file (UTF8) and prints it to stdout"""


def read_file(fileName=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(fileName, encoding="utf-8") as f:
        print(f.read(), end="")
