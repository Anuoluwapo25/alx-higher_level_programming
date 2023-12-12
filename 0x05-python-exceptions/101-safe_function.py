#!/usr/bin/python3
import sys
""" module that execute a function safely"""

def safe_function(fct, *args):
    """function that execute a function"""

    try:
        result = fct(*args)
        return result
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None

def example_function(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
