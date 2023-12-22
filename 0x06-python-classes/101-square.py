#!/usr/bin/python3
"""
Module
A class Square private instance attribute
"""
class Square:
    """
    function that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize object
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        stter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        area
        """
        return self.size ** 2

    def my_print(self):
        """
        print out
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        str
        """
        result = ""
        if self.size == 0:
            result += "\n"
        else:
            for _ in range(self.position[1]):
                result += "\n"
            for _ in range(self.size):
                result += " " * self.position[0] + "#" * self.size + "\n"
        return result.rstrip()
