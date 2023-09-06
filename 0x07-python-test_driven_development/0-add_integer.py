#!/usr/bin/python3
"""
add_integer: adds two integers and return sum
"""


def add_integer(a, b=98):
    """Return the sum of a + b
    Args: a = int/float b = int/float
    """

    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    if isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return int(a + b)
