from abc import ABC, abstractmethod


class Mode(ABC):
    def __init__(self, args):
        self.font = args.font
        self.max_width = float('inf')
        self.max_height = float('inf')

        self.running = True

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
    def draw_frame(self, screen, font, screen_width, screen_height):
        """Draw one frame to the screen.

        Parameters:
            screen: The curses screen to draw to.
            font: The font to use to draw the numbers.
            screen_width: The width of the screen.
            screen_height: The height of the screen.

        Returns: A string that will get displayed to the user if the program
            were to exit now.
        """
