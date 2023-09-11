#!/usr/bin/python3
"""Define an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a class.

    Args:
        obj : The object to check.
        a_class : The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
