from abc import ABC, abstractmethod


class Mode(ABC):
    def __init__(self, args):
        """Initialise the base mode variables.

        Parameters:
            args: The parsed command line arguments.
        """
        self.running = True
        self.termination_string = None

    @staticmethod
    def configure_parser(parser):
        """Configure the command line parser for this mode.

        Parameters:
            parser (ArgumentParser): The parser instance to configure.
        """

    def duration_to_hms(self, duration):
        """Convert a duration (in seconds) to hours, minutes and seconds.

        Parameters:
            duration (int): A duration of time represented as seconds.

        Returns: A tuple containing hours, minutes and seconds.
        """
        hours, remainder = divmod(duration, 60*60)
        minutes, seconds = divmod(remainder, 60)

        return hours, minutes, seconds

    @abstractmethod
    def get_time_string(self):
        """Get the time string to display.

        Returns: A string containing the time to display to the user.
        """
