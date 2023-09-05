#!/usr/bin/python3
"""Module prevents the user from creating new instances attributes"""


class LockedClass:
    """Define a Locked class
    """
    __slots__ = ('first_name', )

    def setattr(self, name, value):
        """Defines the attribute

        Args:
            name : first_name
            value : first_name
        """
        if name == 'first_name':
            self.__dict__[name] = value
