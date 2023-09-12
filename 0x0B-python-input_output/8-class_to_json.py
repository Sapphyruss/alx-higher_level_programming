#!/usr/bin/python3
"""The module returns the dictionary description"""


def class_to_json(obj):
    """Define a function that return the dict description

    Args:
        obj : class to return it's dictionary

    Returns:
        obj dictionary: the obj dictionary
    """
    return obj.__dict__
