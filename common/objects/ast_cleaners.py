"""
The module contains tools for processing AST trees. Each of the
handlers is a descendant of the NodeTransformer class, which is
the preferred means for working with classes of the ast module.
"""

from ast import NodeTransformer

from ast import (
    AnnAssign,
    AsyncFunctionDef,
    Assign,
    Expr,
    FunctionDef,
    ClassDef,
    Constant,
    Module,
)

from typing import Self


class TypeHintCleaner(NodeTransformer):
    """
    Descendant of the NodeTransformer class, designed to remove type hints.
    """

    __slots__ = []

    def visit_FunctionDef(  # pylint: disable=invalid-name
        self: Self,
        node: FunctionDef | AsyncFunctionDef
    ) -> FunctionDef | AsyncFunctionDef:
        """
        Method for removing type annotations in functions.
        For example, the following transformation takes place:

        ```
        def foo(bar: int, baz: None | List[str]) -> Dict[int, str]:
            ...
        ```

        Will be transformed to:

        ```
        def foo(bar, baz):
            ...
        ```
        """

        self.generic_visit(node)

        node.returns = None
        for argument in node.args.args:
            argument.annotation = None

        if node.args.vararg is not None:
            node.args.vararg.annotation = None

        if node.args.kwarg is not None:
            node.args.kwarg.annotation = None

        return node

    def visit_AsyncFunctionDef(  # pylint: disable=invalid-name
        self: Self,
        node: AsyncFunctionDef
    ) -> AsyncFunctionDef:
        """
        Method for removing type annotations in async functions.
        For example, the following transformation takes place:

        ```
        async def foo(bar: int, baz: None | List[str]) -> Dict[int, str]:
            ...
        ```

        Will be transformed to:

        ```
        async def foo(bar, baz):
            ...
        ```
        """

        return self.visit_FunctionDef(node)

    def visit_AnnAssign(self: Self, node: AnnAssign) -> Assign:  # pylint: disable=invalid-name
        """
        Method for removing type annotations in variables annotations.
        For example, the following transformation takes place:

        ```
        money: float
        money = 400.25
        price: int = 399
        ```

        Will be transformed to:

        ```
        money = 400.25
        price = 399
        ```
        """

        if node.value is None:
            return None

        return Assign(
            lineno=node.lineno,
            targets=[node.target],
            value=node.value,
        )


class UnusedConstantCleaner(NodeTransformer):
    """
    Descendant of the NodeTransformer class, designed to remove unused constants.
    """

    __slots__ = []

    def clean(
        self: Self,
        node: ClassDef | FunctionDef | AsyncFunctionDef | Module
    ) -> ClassDef | FunctionDef | AsyncFunctionDef | Module:
        """
        A method designed to rid nodes of unused constants.
        For example, the following transformation takes place:

        ```
        '''
        Some docstring
        '''

        async def bar():
            '''
            Bar docstring
            '''
            ...

        'Hello!'
        2023

        class A(object):
            '''
            A docstring
            '''

            def baz():
                '''
                Baz docstring
                '''
                ...
        ```

        Will be transformed to:

        ```
        async def bar():
            ...

        class A(object):
            def baz():
                ...
        ```
        """

        approved_nodes = []

        for childnode in node.body:
            if not isinstance(childnode, Expr):
                approved_nodes.append(childnode)
                continue

            if not isinstance(childnode.value, Constant):
                approved_nodes.append(childnode)

        node.body = approved_nodes
        return node

    def visit_ClassDef(self: Self, node: ClassDef) -> ClassDef:  # pylint: disable=invalid-name
        """
        A method designed to clean classes from unused constants.
        To get some examples look at method `clean`.
        """

        self.generic_visit(node)
        return self.clean(node)

    def visit_FunctionDef(self: Self, node: FunctionDef) -> FunctionDef:  # pylint: disable=invalid-name
        """
        A method designed to clean functions from unused constants.
        To get some examples look at method `clean`.
        """

        self.generic_visit(node)
        return self.clean(node)

    def visit_AsyncFunctionDef(  # pylint: disable=invalid-name
        self: Self,
        node: AsyncFunctionDef
    ) -> AsyncFunctionDef:
        """
        A method designed to clean async functions from unused constants.
        To get some examples look at method `clean`.
        """

        self.generic_visit(node)
        return self.clean(node)

    def visit_Module(self: Self, node: Module) -> Module:  # pylint: disable=invalid-name
        """
        A method designed to clean program's body from unused constants.
        To get some examples look at method `clean`.
        """

        self.generic_visit(node)
        return self.clean(node)
