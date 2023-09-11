#!/usr/bin/python3
"""Define a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square."""

    def __init__(self, size):
        """Init a new square.

        Args:
            size : The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
