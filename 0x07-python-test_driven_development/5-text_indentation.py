#!/usr/bin/python3
"""
Text indentation
"""

def text_indentation(text):
    """print text with two lines after [".", "?", ":"]
    Args:
        text: input
    Raise:
        TypeError: if text is not a string
    module to indentify string(txt)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    newline_chars = ['.', '?', ':']

    current_line = ""
    for char in text:
        current_line += char
        if char in newline_chars:
            print(current_line.strip())
            print("")
            current_line = ""

    if current_line:
        print(current_line.strip())
        print(end="")
