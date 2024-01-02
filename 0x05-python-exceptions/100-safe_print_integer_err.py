#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    status = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        status = False
        print("Exception: {}".format(str(e)), file=sys.stderr)
    finally:
        return status
