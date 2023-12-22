#!/usr/bin/python3

"""
module
that append
"""

def append_after(filename="", search_string="", new_string=""):
    """
    function append_after
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string + end="")
    except Exception as e:
        print(f"An error occurred: {e}")
