#!/usr/bin/python3
"""This module write to a txt file"""


def write_file(filename="", text=""):
    """This function write to a txt file

    Args:
        filename : File to be written into to "".
        text : Text to be written to "".

    Returns:
        int: number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
