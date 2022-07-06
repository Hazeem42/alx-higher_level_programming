#!/usr/bin/python3
"""Define a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTFB text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
