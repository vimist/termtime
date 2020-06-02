"""TermTime.

A terminal based stopwatch, clock and extendable to any other time related task.
"""

from setuptools import setup


setup(
    name='termtime',
    version='0.2.2',
    author='Vimist',
    description='Stopwatch, Timer, Clock - All in the terminal',
    url='https://github.com/vimist/termtime',
    keywords='terminal timer clock stopwatch',
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators'
    ],
    packages=['termtime', 'termtime.fonts', 'termtime.modes'],
    entry_points={
        'console_scripts' : [
            'termtime=termtime.__main__:main'
        ]
    }
)
