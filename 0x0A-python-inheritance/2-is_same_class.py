#!/usr/bin/python3
"""Define a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns:
        If obj is an instance of a_class - True.
        Else - False.
    """
    if type(obj) == a_class:
        return True
    return False
