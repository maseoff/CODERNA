"""
A module that provides functionality for working with files
"""

def get_total_lines(path_to_file: str) -> int:
    """
    Returns the total number of lines in the given file.
    """

    with open(file=path_to_file, mode="r", encoding="utf-8") as file:
        return sum(1 for _ in file)
