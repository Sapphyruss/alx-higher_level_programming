#!/usr/bin/python3
"""The module return a JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Define a function that convert my_obj into json

    Args:
        my_obj: object to be converted into JSON

    Returns:
        JSON: json representation
    """
    return json.dumps(my_obj)
