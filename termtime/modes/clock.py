import time

from termtime.modes.mode import Mode


class Clock(Mode):
    """Display a 24 hour clock.
    """

    def get_time_string(self):
        """Get the current time.

        Returns: The current time as a string.
        """
        return time.strftime('%H:%M:%S', time.localtime())
