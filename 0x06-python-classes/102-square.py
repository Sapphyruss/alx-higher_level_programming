#!/usr/bin/python3
# 102-square.py
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Init a new square.

        Args:
            size : The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """The current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """The == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """The != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """The < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """The <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """The > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """The >= compmarison to a Square."""
        return self.area() >= other.area()
