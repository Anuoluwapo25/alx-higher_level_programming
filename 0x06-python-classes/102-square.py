#!/usr/bin/python3
"""
Module
A class Square
private instance attribute
"""
class Square:
    """
    function that
    """
    def __init__(self, size=0):
        """
        initialises
        """
        self.size = size

    @property
    def size(self):
        """
        getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        area of square
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        eq
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        ne
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        gt
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        ge
        """
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        """
        lt
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        le
        """
        return self.__lt__(other) or self.__eq__(other)

