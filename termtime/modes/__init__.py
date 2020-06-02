"""Modes that back TermTime.

New modes can be added easily, use `Clock` and `Stopwatch` as examples and make
sure to import them in this file and add them to the `__all__` list.
"""
from termtime.modes.stopwatch import Stopwatch
from termtime.modes.clock import Clock
from termtime.modes.countdown import Countdown


__all__ = [
    'Stopwatch',
    'Clock',
    'Countdown'
]
