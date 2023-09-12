#!/usr/bin/python3
"""The module writes a class"""


class Student:
    """Defines a Student class
    """
    def __init__(self, first_name, last_name, age):
        """Init Student class

        Args:
            first_name : first name
            last_name : last name
            age : age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=""):
        """retrieve a dictionary representation

        Returns:
            dict: dictionary
        """
        if type(attrs) == list and all(type(attr) == str for attr in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
