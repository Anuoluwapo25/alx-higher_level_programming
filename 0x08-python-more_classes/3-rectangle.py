#!/usr/bin/python3

"""
Module: 
a class Rectangle 
"""


class Rectangle:
    """
    defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        initialize attributes
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        returns an informal string representation of the rectangle
        """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height - 1):
            rectangle += "#" * self.width + "\n"
        rectangle += "#" * self.width
        return rectangle

    @property
    def height(self):
        """
        Getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter
        """
        if type(value) not in [int]:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        """
        Getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter
        """
        if type(value) not in [int]:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    def perimeter(self):
        """
        perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def area(self):
        """
        area of the rectangle
        """
        return (self.__height * self.__width)
