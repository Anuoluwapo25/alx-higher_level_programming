def text_indentation(text):
"""
    Print text with 2 new lines after each of these characters: ., ? and :

    :param text: A string to be formatted
    :type text: str
    :raises TypeError: If the input is not a string

    Examples:
    >>> text_indentation("This is a sample text. It has some sentences? Yes, it does: three of them.")
    This is a sample text
    It has some sentences
    Yes, it does
    three of them

    >>> text_indentation("Another example: This one ends with a colon:")
    Another example
    This one ends with a colon

    >>> text_indentation("No special characters here")
    No special characters here
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    newline_chars = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in newline_chars:
            print(current_line.strip())
            current_line = ""

    if current_line:
        print(current_line.strip())

# Run the doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()
