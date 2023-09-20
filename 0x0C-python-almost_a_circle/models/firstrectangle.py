#!/usr/bin/python3
"""
Module Class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle subclass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance init method

        args:
            width: the width of the rectangle
            height: the height of the rectangle
            x: init variable
            y: init variable
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """returns the area of width * height"""
        return self.width * self.height

    def update(self, *args, **kwargs):
        """update attributes"""
        if args:
            listme = ['id', 'width', 'height', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, listme[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def display(self):
        """print into standard output
        return: N/A
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """print method"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def to_dictionary(self):
        """return the dictionary representation of the Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    @property
    def width(self):
        """width get method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width set method"""
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """height get method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height set method"""
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """x get method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x set method"""
        self.integer_validator2('x', value)
        self.__x = value

    @property
    def y(self):
        """y set method"""
        self.integer_validator2('y', value)
        self.__y = value
