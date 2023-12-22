#!/usr/bin/python3
"""
Module 
A class Square 
"""
class Square:
    """
    defines a class square
    """

    def __init__(self, size=0, position=(0, 0)):
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
        setter
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
        stter
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        area of square
        """
        return self.size ** 2

    def my_print(self):
        """
        prints in stsout
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

