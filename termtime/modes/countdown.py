import time

from termtime.modes.mode import Mode


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

    def get_time_string(self):
        """Get the remaining time on the countdown.

        Returns: The remaining time on the countdown as a string.
        """
        time_delta = self._end_time - time.time()

        if time_delta < 0:
            time_delta = 0
            self.running = False

        elapsed_time = self.duration_to_hms(self._duration - time_delta)
        self.termination_string = \
            'Elapsed time: {:02.0f}:{:02.0f}:{:05.2f}'.format(*elapsed_time)

        hours, minutes, seconds = self.duration_to_hms(time_delta)

        return '{:02.0f}:{:02.0f}:{:05.2f}'.format(hours, minutes, seconds)
