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


def render(value, screen, font, screen_width, screen_height):
    """Render a number to the screen using a given 'font'.

    Parameters:
        value (str): The number to render. Can include ':' and '.' characters.
        screen (curses.window): The curses window to draw to.
        font (list): A font in the `fonts` module. Structure must be the same
            as the `default` font.
        screen_width (int): The width of the available screen.
        screen_height (int): The height of the available screen.
    """
    for size in reversed(font):
        output = []

        size_ok = True
        height = len(size[0])

        if height > screen_height:
            size_ok = False
            continue

        for i in range(height):
            line = ''
            for digit in value:
                line += size[mapping[digit]][i]
                line += ' ' * ceil(height//3)

            output.append(line)

            if len(line) > screen_width:
                size_ok = False
                output = []
                break

        if size_ok:
            break

    output =  output if size_ok else [number]

    width = len(output[0])
    height = len(output)

    for i, line in enumerate(output):
        screen.addstr(
            int(screen_height/2 - height/2) + i,
            int(screen_width/2 - width/2),
            line)
