#!/usr/bin/python3

"""
Module: 101-add_attribute
function that adds a new attribute to an object
if it’s possible
"""

def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.
    Raises a TypeError exception if the object can't have a new attribute.
    """
    if hasattr(obj, '__dict__') or (hasattr(obj, '__slots__') and attribute in obj.__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")

