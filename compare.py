"""
You are in the main file of the CODERNA console application. Please try
not to change anything in this file. If any edits are needed, it is best
to change the behavior of the functions.
"""

import sys

from common.objects.parser import ARGUMENT_PARSER
from common.objects.validator import ARGUMENT_VALIDATOR

from common.utils.file import get_total_lines
from common.utils.metrics import calculate_metric


ALWAYS_FORCE_WRITE = True


def progress_bar(current: int, total: int) -> None:
    """
    An assistant function for creating a progress scale that is
    displayed in the console. Look like this:

    [STATUS] [==========               ] 40%
    """

    percent = int(current / total * 100)
    bars = percent // 4

    sys.stdout.write("\r")
    sys.stdout.write(f"[STATUS] [{('=' * bars).ljust(25)}] {percent}%")
    sys.stdout.flush()


if __name__ == "__main__":

    args = ARGUMENT_PARSER.parse_args()
    if ALWAYS_FORCE_WRITE:
        args.force = True

    ARGUMENT_VALIDATOR.validate_args(args)  # Exits with an error if not valid

    lines = get_total_lines(args.input)
    scores = []

    with open(file=args.input, mode="r", encoding="utf-8") as input_file:
        output_file = open(file=args.output, mode="w", encoding="utf-8")

        for lineno, line in enumerate(input_file):
            stripped_line = line.strip()

            if not stripped_line:
                continue  # Skip blank lines

            path_to_lh, path_to_rh = stripped_line.split()
            with open(path_to_lh, mode="r", encoding="utf-8") as lh_file:
                lh_code = lh_file.read()

            with open(path_to_rh, mode="r", encoding="utf-8") as rh_file:
                rh_code = rh_file.read()

            score = calculate_metric(
                lh_code=lh_code,
                rh_code=rh_code,
                use_percent=args.percent
            )

            output_file.write(f"{score}{'%' if args.percent else ''}\n")
            progress_bar(current=lineno, total=lines)

    output_file.close()
    progress_bar(current=lines, total=lines)
