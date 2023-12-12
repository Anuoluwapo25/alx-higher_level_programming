#!/usr/bin/python3
"""module that prints an integer"""

def magic_calculation(a, b):
    """defines amodule"""

    result = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except Exception:
            result += b + a
            break
    return result

