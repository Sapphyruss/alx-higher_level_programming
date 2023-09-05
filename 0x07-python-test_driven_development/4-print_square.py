#!/usr/bin/python3
"""
Print a square
"""


def print_square(size):
    """print a square with a given size

    Args:
        size : size of square

    Raises:
        TypeError: when size is not an integer
        ValueError: when size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
