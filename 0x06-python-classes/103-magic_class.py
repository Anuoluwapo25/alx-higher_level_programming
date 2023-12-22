#!/usr/bin/python3
"""
module for magicClass
"""
import math

class MagicClass:
    """
    function that implement the class with __inti__ method and arear method
    """
    def __init__(self, radius=0):
        """
        initialize
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        area of square
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        circumference of a square
        """
        return 2 * math.pi * self.__radius

