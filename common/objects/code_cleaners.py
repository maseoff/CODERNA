"""
The module contains tools for code postpocessing. It
is assumed that the AST tree has already been cleared.
Anyway, the point above does not prohibit using the
tool without the AST preprocessing.
"""

from abc import ABC
from abc import abstractmethod

from typing import Self


class CodeCleaner(ABC):
    """
    An anbstract class for code cleaners.
    """

    @abstractmethod
    def apply(self: Self, code: str) -> str:
        """
        An abstract method for code cleaning.
        """


class EmptyLineCleaner(CodeCleaner):
    """
    Descendant of the CodeCleaner class, designed to remove empty lines from code.
    """

    __slots__ = []

    def apply(self: Self, code: str) -> str:
        """
        Removes empty lines from code.
        """

        return "\n".join(
            filter(
                lambda line: line,
                code.split("\n"),
            )
        )


class TrailingWhitespaceCleaner(CodeCleaner):
    """
    Descendant of the CodeCleaner class, designed
    to remove trailing whitespaces from code.
    """

    __slots__ = []

    def apply(self: Self, code: str) -> str:
        return "\n".join(
            map(
                lambda line: line.rstrip(),
                code.split("\n"),
            )
        )
