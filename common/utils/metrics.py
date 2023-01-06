"""
The module describes how to work with metrics that are
used to analyze thedegree of similarity of programs.
"""

from common.utils.levenshtein import levenshtein
from common.utils.format import pyformat


def calculate_metric(
    lh_code: str,
    rh_code: str,
    use_percent: bool = False
) -> float | int:

    """
    Calculates the similarity metric between two written programs.

    @param lh_code: left-hand code to compare
    @param rh_code: right-hand code to compare
    @param use_percent: whether to use percents instead of ratio metric
    @return: The value of the metric
    """

    unsorted_lh_code = pyformat(lh_code, sort_structures=False)
    unsorted_rh_code = pyformat(rh_code, sort_structures=False)

    sorted_lh_code = pyformat(lh_code, sort_structures=True)
    sorted_rh_code = pyformat(rh_code, sort_structures=True)

    unsorted_ratio = get_similarity_ratio(unsorted_lh_code, unsorted_rh_code)
    sorted_ratio = get_similarity_ratio(sorted_lh_code, sorted_rh_code)

    ratio = max(unsorted_ratio, sorted_ratio)  # Choose more strict metric
    return ratio * 100 if use_percent else ratio


def get_similarity_ratio(lh_str: str, rh_str: str) -> float:
    """
    Calculates the similarity ratio between two strings.

    @param lh: left-hand string
    @param rh: right-hand string
    @return: The similarity ratio
    """

    levenshtein_distance = levenshtein(lh_str, rh_str)
    str_length = max(len(lh_str), len(rh_str))

    return 1.0 if str_length == 0 else 1 - levenshtein_distance / str_length
