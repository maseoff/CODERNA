"""
The module describes the console argument parser, which is used to interact
with the internal component of the program from the outside.
"""

from argparse import ArgumentParser


ARGUMENT_PARSER = ArgumentParser(
    prog="python compare.py",
    description="Control the degree of similarity of Python code directly "
    "from the console with use of advanced Levenshtein distance.",
    epilog="Created by @maseoff",
)

ARGUMENT_PARSER.add_argument(
    "input",
    type=str,
    help="The absolute path to the input file. "
    "Required format: a pair of files being compared is written "
    "on the i-th line separated by a space. "
    "Example of a file line: left/path/lh.py right/path/rh.py",
)

ARGUMENT_PARSER.add_argument(
    "output",
    type=str,
    help="The absolute path to the output file. "
    "Output format: the i-th line contains the similarity value "
    "of the i-th pair of the input file. "
    "Example of a file line: 0.79",
)

ARGUMENT_PARSER.add_argument(
    "-f",
    "--force",
    action="store_true",
    help="rewrite output file if it exists",
)

ARGUMENT_PARSER.add_argument(
    "-p",
    "--percent",
    action="store_true",
    help="use percent metric instead of ratio",
)
