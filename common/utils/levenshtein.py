"""
The module is responsible for implementing the Levenshtein algorithm.
"""

from typing import List


def levenshtein(lh_str: str, rh_str: str) -> int:
    """
    Counts the editorial Levenshtein distance between the two strings.
    We use N * M array isntead of (N + 1) * (M + 1) to reach the best
    space and time complexity for the algorithm.

    @param lh_str: left-hand string
    @param rh_str: right-hand string
    @return: The value of the Levenshtein editorial distance
    """

    rows = len(lh_str)
    cols = len(rh_str)

    if rows == 0 or cols == 0:
        return 0

    distance = [[0] * cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):

            lh_symbol = lh_str[row]
            rh_symbol = rh_str[col]

            if lh_symbol == rh_symbol:
                distance[row][col] = get_distance_value(distance, row - 1, col - 1)

            else:
                distance[row][col] = 1 + min(
                    get_distance_value(distance, row, col - 1),
                    get_distance_value(distance, row - 1, col - 1),
                    get_distance_value(distance, row - 1, col),
                )

    return distance[-1][-1]


def get_distance_value(distance: List[List[int]], row: int, col: int) -> int:
    """
    Returns the value of the Levenshtein distance between the two strings
    from the given distance array.

    Due to using N * M array instead of (N + 1) * (M + 1) it is better to
    use such a function for the best performance and readability. Approach
    with using N * M array helps to reduce space and time complexity.

    @param distance: The array with Levenshtein distances
    @param row: The row index
    @param col: The column index
    @return: The value of the Levenshtein distance
    """

    if row == -1 and col == -1:
        return 0

    elif row == -1:
        return col + 1

    elif col == -1:
        return row + 1

    else:
        return distance[row][col]
