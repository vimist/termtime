# TermTime

A command line utility to manage and display time related tasks in the terminal:
- Display a live 24 hour clock
- Start a live stopwatch
- Start a timer

## Installation

```
pip install termtime
```

## Example

Gaps between lines are typically smaller in the terminal, so the below is
usually displayed much clearer.

```
▄▄▄▄ ▄  ▄   ▄▄▄▄ ▄▄▄▄   ▄  ▄ ▄  ▄     ▄  ▄▄▄▄
█  █ █  █ ▄    █ █    ▄ █  █ █  █    ▀█  █  █
█  █ █▄▄█    ▀▀█ ▀▀▀█   █▄▄█ █▄▄█     █  █  █
█  █    █ ▀    █    █ ▀    █    █     █  █  █
▀▀▀▀    ▀   ▀▀▀▀ ▀▀▀▀      ▀    ▀ ▀  ▀▀▀ ▀▀▀▀
```

Automatically scales to the size of the screen!

```
█▀█ █ █ ▄ ▀▀█ █▀▀ ▄ █ █ █▀█   ▄█  █▀█
█ █ █▄█    ▀█ ▀▀█   █▄█ █▀█    █  █▀█
█▄█   █ ▀ ▄▄█ ▄▄█ ▀   █ █▄█ ▄ ▄█▄ █▄█
```

# Usage

```
usage: termtime [-h] [-f {default}] [--max-width MAX_WIDTH]
                [--max-height MAX_HEIGHT]
                {stopwatch,clock, timer} [-t timer_seconds]...

positional arguments:
  {stopwatch,clock,timer}     Modes that termtime supports.

optional arguments:
  -h, --help            show this help message and exit
  -f {default}, --font {default}
                        The font to use to render the output.
  --max-width MAX_WIDTH
                        The maximum width of the output.
  --max-height MAX_HEIGHT
                        The maximum height of the output.
  -t timer_seconds      The starting time for the timer (only for timer mode)
```

# Extendable

- Easily create your own fonts to change the style of the output.
- Create new modes and contribute them back to the project to extend the
  functionality of TermTime.
