"""Helper methods to render the large fonts to the terminal.
"""
from math import ceil

from termtime.fonts.default import font as default


__all__ = [
    'default'
]


# Maps from values to indexes in the font list.
mapping = {
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    '0': 9,
    ':': 10,
    '.': 11,
}


def render(font, number, max_size=(float('inf'), float('inf'))):
    """Render a number using a given 'font'.

    Parameters:
        font (list): A font in the `fonts` module. Structure must be the same
            as the `default` font.
        number (int/str): The number to render. Can include ':' and '.'
            characters.
        max_size (tuple): The max width and height of the font, the largest
            font will be used.

    Returns (tuple): A tuple containing a list of lines that can be printed to
        the terminal (line by line), the width of the text and the hiehgt of
        the text.
    """
    for size in reversed(font):
        output = []

        size_ok = True
        height = len(size[0])

        if height > max_size[1]:
            size_ok = False
            continue

        for i in range(height):
            line = ''
            for digit in str(number):
                line += size[mapping[digit]][i]
                line += ' ' * ceil(height//3)

            output.append(line)

            if len(line) > max_size[0]:
                size_ok = False
                output = []
                break

        if size_ok:
            break

    output =  output if size_ok else [str(number)]

    width = len(output[0])
    height = len(output)

    return output, width, height
