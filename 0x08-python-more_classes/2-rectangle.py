#!/usr/bin/python3
""" modules that defines a rectangle by private instance attribute"""

class Rectangle:
    """ defines a rectangle by private instance attribute"""

    def __init__(self, width=0, height=0):
        self._width = 0  
        self._height = 0

        self.width = width
        self.height = height

    def width(self):
        return self._width

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def height(self):
        return self._height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)


