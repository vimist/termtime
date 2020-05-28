import time
import sys

from termtime.modes.mode import Mode
from termtime.fonts import render


class Timer(Mode):
    """Display a timer that starts at the argument timer when the program is launched, and go back to zero.
    """
    def __init__(self, args):
        super().__init__(args)

        self.start_time = time.time()+self.timer


    def draw_frame(self, screen, screen_width, screen_height):
        """Draw the stopwatch to the screen.

        Returns: A string containing the total elapsed time.
        """
        max_width = min(self.max_width, screen_width)
        max_height = min(self.max_height, screen_height)

        time_delta = self.start_time - time.time()

        if time_delta <= 0:
            hours, remainder = divmod(self.timer, 60*60)
            minutes, seconds = divmod(remainder, 60)
            time_string = '{:02.0f}:{:02.0f}:{:05.2f}'.format(hours, minutes, seconds)
            return 'Elapsed time: {}'.format(time_string), True

        hours, remainder = divmod(time_delta, 60*60)
        minutes, seconds = divmod(remainder, 60)

        time_string = '{:02.0f}:{:02.0f}:{:05.2f}'.format(
            hours, minutes, seconds)

        numbers, width, height = render(
            self.font, time_string, (max_width, max_height))

        for i, line in enumerate(numbers):
            screen.addstr(
                int(screen_height/2 - height/2) + i,
                int(screen_width/2 - width/2),
                line)

        return 'Elapsed time: {}'.format(time_string), False
