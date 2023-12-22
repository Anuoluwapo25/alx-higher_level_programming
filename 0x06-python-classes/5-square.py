#!/usr/bin/python3
"""
Module 
A class Square that defines a square by
private instance attribute
"""


class Square:
    """
    defines a class square 
    with size attribute size 
    """
    def __init__(self, size=0):
        """
        Initialize object
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        print the square with the character #
        """
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
