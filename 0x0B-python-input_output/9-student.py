#!/usr/bin/python3
"""The module writes a class"""


class Student:
    """Define a Student class
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

    def to_json(self):
        """retrieve a dictionary representation

        Returns:
            dict: dictionary
        """
        return self.__dict__
