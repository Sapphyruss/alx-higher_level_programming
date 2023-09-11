#!/usr/bin/python3
"""Define a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add new attribute to an object if possible.

    Args:
        obj : Object to add an attribute to.
        att : Name of the attribute to add to obj.
        value : Value of att.
    Raises:
        TypeError: If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
