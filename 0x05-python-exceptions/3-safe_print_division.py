#!/usr/bin/python3
def safe_print_division(a, b):
    c = None
    try:
        c = a / b
    except (TypeError, ZeroDivisionError):
        return None
    finally:
        if c is not None:
            print("Inside result: {}".format(c))
            return c
        else:
            print("Inside result: {}".format(None))
