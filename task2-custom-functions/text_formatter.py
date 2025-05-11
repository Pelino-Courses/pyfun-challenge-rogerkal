"""
text_formatter.py

This script provides a custom function `format_text` that formats strings
based on alignment and width, with built-in validation and error handling.

Functions:
    - format_text(text, width=50, align='left')

Examples:
    >>> format_text("Hello", 10)
    'Hello     '

    >>> format_text("Hi", 10, align='center')
    '    Hi    '
"""

def format_text(text, width=50, align='left'):
    """
    Format a given string to fit within a specified width and alignment.

    Parameters:
    - text (str): The input string to format.
    - width (int): The total width to format within. Default is 50.
    - align (str): Alignment type: 'left', 'right', or 'center'. Default is 'left'.

    Returns:
    - str: Formatted string aligned within the given width.

    Raises:
    - TypeError: If text is not a string or width is not an integer.
    - ValueError: If align is invalid or width is smaller than the text length.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(width, int):
        raise TypeError("width must be an integer")
    if align not in ['left', 'right', 'center']:
        raise ValueError("align must be 'left', 'right', or 'center'")
    if width < len(text):
        raise ValueError("width must be greater than or equal to text length")

    if align == 'left':
        return text.ljust(width)
    elif align == 'right':
        return text.rjust(width)
    else:
        return text.center(width)

# Example test cases with error handling
if __name__ == "__main__":
    examples = [
        ("Hello world!", 20, 'left'),
        ("Python", 15, 'right'),
        ("Center this", 30, 'center'),
        (123, 10, 'left'),               # TypeError
        ("Too narrow", 5, 'center'),     # ValueError
        ("Test", 10, 'diagonal')         # ValueError
    ]

    for i, (txt, w, a) in enumerate(examples):
        print(f"\nExample {i + 1}:")
        try:
            formatted = format_text(txt, w, a)
            print(f"'{formatted}'")
        except Exception as e:
            print("Error:", e)


