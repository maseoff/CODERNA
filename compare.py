"""
You are in the main file of the CODERNA console application. Please try
not to change anything in this file. If any edits are needed, it is best
to change the behavior of the functions.
"""

import common.utils.stdout as stdout

from common.objects.parser import ARGUMENT_PARSER
from common.objects.validator import ARGUMENT_VALIDATOR

from common.utils.file import get_total_lines
from common.utils.metrics import calculate_metric


ALWAYS_FORCE_WRITE = True


if __name__ == "__main__":

    args = ARGUMENT_PARSER.parse_args()
    if ALWAYS_FORCE_WRITE:
        args.force = True

    ARGUMENT_VALIDATOR.validate_args(args)  # Exits with an error if not valid

    lines = get_total_lines(args.input)
    scores = []

    stdout.message(title="ANALYSIS", msg="Starting to compare files.")
    stdout.progress_bar(current=0, total=lines, title="ANALYSIS")

    with open(file=args.input, mode="r", encoding="utf-8") as input_file:
        output_file = open(file=args.output, mode="w", encoding="utf-8")

        for lineno, line in enumerate(input_file, start=1):
            stripped_line = line.strip()

            if not stripped_line:
                output_file.write("\n")
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
            stdout.progress_bar(current=lineno, total=lines, title="ANALYSIS")

    output_file.close()
    stdout.message(title="ANALYSIS", msg="Status: FINISHED.")
