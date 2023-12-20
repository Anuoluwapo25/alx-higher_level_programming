#!/usr/bin/python3
"""
module that prints square with the character #
"""

def print_square(size):
    """
    A function that prints a square with the character #

    Args:
    size: the size lenght of the square

    Raise:
    TypeError with message "size must be an interger
    ValueError: with message "size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
