"""
A module describing the heirs of NodeTransformer, designed to sort
program objects in a special order. This approach makes it possible
to increase accuracy in cases when functions were swapped when cheating.
"""

from ast import NodeTransformer

from ast import (
    AsyncFunctionDef,
    ClassDef,
    FunctionDef,
    Import,
    ImportFrom,
    Module,
)

from typing import List, TypeVar, Self


Node = TypeVar("Node")


class ClassSorter(NodeTransformer):
    """
    A class that implements the sorting of classes in lexicographic order.
    """

    __slots__ = []

    def sort_classes(
        self: Self,
        node: AsyncFunctionDef | FunctionDef | ClassDef | Module
        ) -> AsyncFunctionDef | FunctionDef | ClassDef | Module:

        """
        Sorts the classes in the given node.
        """

        class_nodes: List[ClassDef] = []
        import_nodes: List[Import] = []
        import_from_nodes: List[ImportFrom] = []
        rest_nodes: List[Node] = []

        for childnode in node.body:
            if isinstance(childnode, ClassDef):
                class_nodes.append(childnode)

            elif isinstance(childnode, Import):
                import_nodes.append(childnode)

            elif isinstance(childnode, ImportFrom):
                import_from_nodes.append(childnode)

            else:
                rest_nodes.append(childnode)

        class_nodes.sort(key=lambda async_function: async_function.name)

        node.body = (
            import_nodes + import_from_nodes + \
            class_nodes + \
            rest_nodes
        )

        return node

    def visit_AsyncFunctionDef(  # pylint: disable=invalid-name
        self: Self,
        node: AsyncFunctionDef
    ) -> AsyncFunctionDef:

        """
        Sorts the classes in async functions.
        """

        self.generic_visit(node)
        return self.sort_classes(node)

    def visit_FunctionDef(self: Self, node: FunctionDef) -> FunctionDef:  # pylint: disable=invalid-name
        """
        Sorts the classes in functions.
        """

        self.generic_visit(node)
        return self.sort_classes(node)

    def visit_ClassDef(self: Self, node: ClassDef) -> ClassDef:  # pylint: disable=invalid-name
        """
        Sorts the classes in classes.
        """

        self.generic_visit(node)
        return self.sort_classes(node)

    def visit_Module(self: Self, node: Module) -> Module:  # pylint: disable=invalid-name
        """
        Sorts the classes in the main program's body.
        """

        self.generic_visit(node)
        return self.sort_classes(node)


class FunctionSorter(NodeTransformer):
    """
    A class that implements the sorting of functions in lexicographic order.
    """

    def sort_functions(
        self: Self,
        node: AsyncFunctionDef | FunctionDef | ClassDef | Module
        ) -> AsyncFunctionDef | FunctionDef | ClassDef | Module:

        """
        Sorts the functions in the given node.
        """

        async_function_nodes: List[AsyncFunctionDef] = []
        function_nodes: List[FunctionDef] = []
        import_nodes: List[Import] = []
        import_from_nodes: List[ImportFrom] = []
        rest_nodes: List[Node] = []

        for childnode in node.body:
            if isinstance(childnode, AsyncFunctionDef):
                async_function_nodes.append(childnode)

            elif isinstance(childnode, FunctionDef):
                function_nodes.append(childnode)

            elif isinstance(childnode, Import):
                import_nodes.append(childnode)

            elif isinstance(childnode, ImportFrom):
                import_from_nodes.append(childnode)

            else:
                rest_nodes.append(childnode)

        async_function_nodes.sort(key=lambda async_function: async_function.name)
        function_nodes.sort(key=lambda function: function.name)

        node.body = (
            import_nodes + import_from_nodes + \
            async_function_nodes + function_nodes + \
            rest_nodes
        )

        return node

    def visit_AsyncFunctionDef(  # pylint: disable=invalid-name
        self: Self,
        node: AsyncFunctionDef
    ) -> AsyncFunctionDef:

        """
        Sorts the functions in async functions.
        """

        self.generic_visit(node)
        return self.sort_functions(node)

    def visit_FunctionDef(self: Self, node: FunctionDef) -> FunctionDef:  # pylint: disable=invalid-name
        """
        Sorts the functions in functions.
        """

        self.generic_visit(node)
        return self.sort_functions(node)

    def visit_ClassDef(self: Self, node: ClassDef) -> ClassDef:  # pylint: disable=invalid-name
        """
        Sorts the functions in classes.
        """

        self.generic_visit(node)
        return self.sort_functions(node)

    def visit_Module(self: Self, node: Module) -> Module:  # pylint: disable=invalid-name
        """
        Sorts the functions in the main program's body.
        """

        self.generic_visit(node)
        return self.sort_functions(node)
