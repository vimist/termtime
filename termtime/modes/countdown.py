import time
import sys

from termtime.modes.mode import Mode
from termtime.fonts import render


class Countdown(Mode):
    """Display a countdown timer that counts down to zero.
    """

    def __init__(self, args):
        super().__init__(args)

        self._duration = args.duration
        self._end_time = time.time() + self._duration

    @staticmethod
    def configure_parser(parser):
        """Add the duration argument to this subcommand.

        Parameters:
            parser (ArgumentParser): The parser instance to configure.
        """
        parser.add_argument(
            'duration', type=int,
            help='The duration of the countdown timer in seconds.')

    def draw_frame(self, screen, screen_width, screen_height):
        """Draw the countdown timer to the screen.

        Returns: A string containing the total elapsed time.
        """
        max_width = min(self.max_width, screen_width)
        max_height = min(self.max_height, screen_height)

        time_delta = self._end_time - time.time()

        if time_delta < 0:
            time_delta = 0
            self.running = False

        hours, minutes, seconds = self.duration_to_hms(time_delta)

        time_string = '{:02.0f}:{:02.0f}:{:05.2f}'.format(
            hours, minutes, seconds)

        numbers, width, height = render(
            self.font, time_string, (max_width, max_height))

        for i, line in enumerate(numbers):
            screen.addstr(
                int(screen_height/2 - height/2) + i,
                int(screen_width/2 - width/2),
                line)

        return 'Elapsed time: {:02.0f}:{:02.0f}:{:05.2f}'.format(
            *self.duration_to_hms(self._duration - time_delta ))
