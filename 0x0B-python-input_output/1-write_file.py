#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """write a string to a UTFB text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file,
    Returns:
        Thenumber of characters written.
    """
    with open(fiename, "w", encoding="utf-8") as f:
        return f.write(text)
