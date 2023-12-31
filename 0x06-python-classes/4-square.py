#!/usr/bin/python3
"""module that demonstrate a private instance attribute"""

class Square:
    """
    class that defines private instance attribute
    public instance
    """
    def __init__(self, size=0):
        self.size = size

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

