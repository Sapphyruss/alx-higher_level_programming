#!/usr/bin/python3
"""Module append to a txt file"""


def append_write(filename="", text=""):
    """This function append to a txt file

    Args:
        filename : File to be written into. Defaults to "".
        text : text to be written. Defaults to "".

    Returns:
        int: Number of characters written
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return (file.write(text))
