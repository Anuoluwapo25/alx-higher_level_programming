#!/usr/bin/python3
"""This module defines class square"""

class Square:
    """defines a class square"""

    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, new_size):
        self.__size = new_size
