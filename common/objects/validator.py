"""
This module describes the behavior of the input argument validator. The basic
principle of its operation is that in case of any inaccuracy, immediately
complete the work by throwing an error.
"""

import ast
import re

import os
import sys

from argparse import Namespace
from typing import List, Self


class ArgumentValidator(object):
    """
    A class that implements the functionality
    of the command-line argument validator.
    """

    __slots__ = [
        "_args",
        "_errors",
    ]

    def __init__(self: Self) -> None:
        self._args: Namespace | None = None
        self._errors: List[str] | None = None

    def validate_args(self: Self, args: Namespace) -> None:
        """
        Validate all the provided arguments.
        """

        self._args = args
        self._errors = []

        self.__validate_input()
        self.__validate_output()

        self.__get_validation_status()

    def __validate_input(self: Self) -> None:
        """
        Validates the input file.
        """

        if not os.path.exists(self._args.input):
            self._errors.append(
                "The input file does not seem to exist. "
                "Please check the specified path."
            )
            return

        if not self.__is_valid_input_format():
            self._errors.append(
                "The input file does not adhere to the required format. It is "
                "possible to get acquainted with the format of the input file "
                "through the use of the command: python comapre.py -h"
            )
            return

        self.__validate_files_to_compare()

    def __is_valid_input_format(self: Self) -> bool:
        """
        Validates the input file format. Expected that the input file exists.
        """

        has_valid_format = True
        with open(
            file=self._args.input,
            mode="r",
            encoding="utf-8"
        ) as input_file:

            for lineno, line in enumerate(input_file, start=1):
                stripped_line = line.strip()

                if not stripped_line:
                    continue  # Skip blank lines

                if not re.match(r"^[^\s]+ [^\s]+$", stripped_line):
                    has_valid_format = False

                    self._errors.append(
                        f"Line {lineno} of the input file does not comply "
                        "with the required input file format. Detailed "
                        "information will be provided below."
                    )

        return has_valid_format

    def __validate_files_to_compare(self: Self) -> None:
        """
        Validates the input files which are required to be compared.
        Expected that the input files exists and follows the format.
        """

        with open(
            file=self._args.input,
            mode="r",
            encoding="utf-8"
        ) as input_file:

            for lineno, line in enumerate(input_file, start=1):
                stripped_line = line.strip()

                if not stripped_line:
                    continue  # Skip blank lines

                for path in stripped_line.split():
                    if not re.match(r".+.py", path):
                        self._errors.append(
                            f"Line {lineno} of the input file has a wrong "
                            "file: doesn't have .py extension. Please change "
                            "the extension or delete the following path from "
                            f"the input file: {path}"
                        )
                        continue

                    if not os.path.exists(path):
                        self._errors.append(
                            f"Line {lineno} of the input file has a path that "
                            "does not exist. Please check if the provided "
                            f"path is correct and try again: {path}"
                        )
                        continue

                    # Check if the file has valid Python code
                    try:
                        with open(
                            file=path,
                            mode="r",
                            encoding="utf-8"
                        ) as file:
                            ast.parse(file.read())

                    except SyntaxError:
                        self._errors.append(
                            f"Line {lineno} of the input file has a Python "
                            "file with syntax errors. Please fix the problem "
                            f"or avoid comparing the following one: {path}"
                        )

    def __validate_output(self: Self) -> None:
        """
        Validates the output file
        """

        if os.path.exists(self._args.output) and not self._args.force:
            self._errors.append(
                "The output file already exists at the specified path. Set "
                "the -f or --force flag to use this file. Please note that "
                "the past data will be permanently erased."
            )

    def __get_validation_status(self: Self) -> None:
        """
        Checks validation status. If any errors were encountered,
        then lists them to the console and exits the program.
        """

        for error in self._errors:
            sys.stdout.write(f"[ERROR] {error}\n")

        if self._errors:
            sys.stdout.flush()
            sys.exit(1)

        self._args = None
        self._errors = None


ARGUMENT_VALIDATOR = ArgumentValidator()
