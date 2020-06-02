import time

from termtime.modes.mode import Mode


class Stopwatch(Mode):
    """Display a stopwatch that starts from the moment the program is launched.
    """
    def __init__(self, args):
        super().__init__(args)

        self.start_time = time.time()

    def get_time_string(self):
        """Get the current ellapsed time.

        Returns: The current ellapsed time as a string.
        """
        time_delta = time.time() - self.start_time

        hours, minutes, seconds = self.duration_to_hms(time_delta)

        elapsed_time = '{:02.0f}:{:02.0f}:{:05.2f}'.format(
            hours, minutes, seconds)

        self.termination_string = 'Elapsed time: {}'.format(elapsed_time)

        return elapsed_time
