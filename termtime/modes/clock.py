import time

from termtime.modes.mode import Mode
from termtime.fonts import render


class Clock(Mode):
    """Display a 24 hour clock.
    """

    def draw_frame(self, screen, screen_width, screen_height):
        """Draw the clock to the screen.
        """
        max_width = min(self.max_width, screen_width)
        max_height = min(self.max_height, screen_height)

        rendered_time, width, height = render(
            self.font, time.strftime('%H:%M:%S', time.localtime()),
            (max_width, max_height))

        for i, line in enumerate(rendered_time):
            screen.addstr(
                int(screen_height/2 - height/2) + i,
                int(screen_width/2 - width/2),
                line)
        
        return None, False
