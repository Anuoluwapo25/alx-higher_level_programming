#!/usr/bin/python3
class Rectangle:
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

    def __str__(self):
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


