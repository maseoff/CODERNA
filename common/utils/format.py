"""
The module describes the functionality intended for formatting the
transmitted code. It is used for preprocessing the code as text before
applying the Levenshtein algorithm.
"""

import ast

from common.objects.ast_cleaners import (
    TypeHintCleaner,
    UnusedConstantCleaner,
)

from common.objects.ast_sorters import (
    ClassSorter,
    FunctionSorter,
)

from common.objects.code_cleaners import (
    EmptyLineCleaner,
    TrailingWhitespaceCleaner,
)


def pyformat(code: str, sort_structures: bool = True) -> str:
    """
    Formats code written in the Python programming language for subsequent
    processing in the internal component of the process. Please note that
    formatting is not done to improve the readability of the code, but to
    increase the accuracy of the metric. In this regard, the function should
    not be perceived as a linter. There is no guarantee that the code after
    processing this function will still be able to compile

    @param code: Python code that should be formatted
    @param sort_structures: Whether to sort functions and classes by
    lexicographic order
    @return: Formatted Python code
    """

    # Processed automatically:
    # - Comments -> Reduced
    # - The quotes style -> To the unified style

    tree = ast.parse(code)
    for ast_cleaner in [
        TypeHintCleaner,
        UnusedConstantCleaner,
    ]:
        tree = ast_cleaner().visit(tree)

    if sort_structures:
        for ast_sorter in [
            ClassSorter,
            FunctionSorter,
        ]:
            tree = ast_sorter().visit(tree)

    code = ast.unparse(tree)
    for code_cleaner in [
        TrailingWhitespaceCleaner,
        EmptyLineCleaner,
    ]:
        code = code_cleaner().apply(code)

    return code
