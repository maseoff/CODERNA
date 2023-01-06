"""
This module describes the behavior of the functions
which are used when working with stdout
"""

import sys


def progress_bar(current: int, total: int, title: str) -> None:
    """
    An assistant function for creating a progress scale that is
    displayed in the console. Looks like this:

    [STATUS] [==========               ] 40%

    Puts '\n' symbol only after reaching 100%.

    @param current: current units
    @param total: maximal units
    @param title: title for the progress scale
    """

    percent = int(current / total * 100) if total != 0 else 100
    bars = percent // 4

    sys.stdout.write("\r")
    sys.stdout.write(f"[{title}] [{('=' * bars).ljust(25)}] {percent}% ")
    sys.stdout.flush()

    if percent == 100:
        sys.stdout.write("\n")
        sys.stdout.flush()


def message(title: str, msg: str) -> None:
    """
    An assistant function for printing messages in the console.
    """

    sys.stdout.write(f"[{title}] {msg}\n")
    sys.stdout.flush()


def newline() -> None:
    """
    An assistant function for printing newilne in the console.
    """

    sys.stdout.write("\n")
    sys.stdout.flush()
