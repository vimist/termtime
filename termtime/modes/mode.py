from abc import ABC, abstractmethod


class Mode(ABC):
    def __init__(self, args):
        self.font = args.font
        self.max_width = float('inf')
        self.max_height = float('inf')

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
