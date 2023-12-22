#!/usr/bin/python3
"""A class that defines a rectangle by private instance attribute width and height"""

class Rectangle:
    """ defines a rectangle"""
    def __init__(self, width=0, height=0):
        self._width = 0 
        self._height = 0

        self.width = width
        self.height = height

    def width(self):
        """getter
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        getter
        """
        return self._height


    @height.setter
    def height(self, value):
        """
        setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """
        Returns:
            area of the rectangle
        """
        return self._width * self._height

    def perimeter(self):
        """
        Return peremeter
        """
        if self._width == 0 or self._height == 0:
            return 0
        else:
            return 2 * (self._width + self._height)

    def __str__(self):
        """
        returns an informal string representation of the rectangle
        """
        if self._width == 0 or self._height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self._height):
                rectangle_str += "#" * self._width
                if i < self._height - 1:
                    rectangle_str += "\n"
            return rectangle_str

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"


