#!/usr/bin/python3
"""The module returns a python object from JSON"""
import json


def from_json_string(my_str):
    """Define a function that convert my_str from json

    Args:
        my_str : object to be converted into python object

    Returns:
        obj: python object
    """
    return json.loads(my_str)
