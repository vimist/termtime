"""TermTime.

The CLI entry point into the program.
"""

import argparse
import curses
import time

from termtime import modes
from termtime import fonts


def loop(stdscr, args):
    """The main program loop.

    Parameters:
        stdscr: The curses screen to write to.
        args: A data structure containing the values from the command line
            parameters.

    Returns: A simple string to be printed on program termination.
    """
    curses.curs_set(0)

    mode = args.mode(args)

    try:
        while mode.running:
            stdscr.clear()

            screen_height, screen_width = stdscr.getmaxyx()
            value = mode.get_time_string()

            fonts.render(value, stdscr, args.font, screen_width, screen_height)

            stdscr.refresh()
            time.sleep(0.12345)
    except KeyboardInterrupt:
        pass

    return mode.termination_string


def main():
    """The main entry point."
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--font', choices=fonts.__all__, default=fonts.default,
        help='The font to use to render the output.')
    parser.add_argument(
        '--max-width', type=int, default=float('inf'),
        help='The maximum width of the output.')
    parser.add_argument(
        '--max-height', type=int, default=float('inf'),
        help='The maximum height of the output.')
    parser.set_defaults(mode=modes.Stopwatch)  # Default to the stopwatch

    subparsers = parser.add_subparsers(
        help='Modes that termtime supports.')

    # Add all the available modes
    for mode_name in modes.__all__:
        mode = getattr(modes, mode_name)
        subparser = subparsers.add_parser(
            mode_name.lower())
        mode.configure_parser(subparser)
        subparser.set_defaults(mode=mode)

    termination_string = curses.wrapper(loop, parser.parse_args())

    if termination_string is not None:
        print(termination_string)
