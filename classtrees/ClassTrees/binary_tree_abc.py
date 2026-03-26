from abc import ABC, abstractmethod

class Position:
    def __init__(self, handle):
        self.handle = handle


class BinaryTree(ABC):
    """
    Abstract base class for binary trees.
    """

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns a string representation of the tree. NOTE
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Removes all elements from the tree.
        """
        pass

    @abstractmethod
    def add_root(self, element: object) -> Position:
        """
        Add element as a root node, overriding existing one (if any).
        """
        pass

    @abstractmethod
    def add_left_child(self, pos: Position, element: object) -> Position:
        """
        Add element as a left child node, overriding existing one (if any).
        """
        pass

    @abstractmethod
    def add_right_child(self, pos: Position, element: object) -> Position:
        """
        Add element as a right child node, overriding existing one (if any).
        """
        pass

    @abstractmethod
    def remove_subtree(self, pos: Position):
        """
        Removes the entire subtree at position.
        """
        pass

    @abstractmethod
    def remove(self, pos: Position):
        """
        Removes the node at given position if at a leaf, otherwise raises IndexError exception.
        """
        pass

    @abstractmethod
    def replace(self, pos: Position, element: object) -> object:
        """
        Replaces the element at given position with a new element, returning the original.
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Returns True if tree is empty, otherwise False.
        """
        pass

    @abstractmethod
    def root(self) -> Position | None:
        """
        Returns the root of the tree if present, otherwise None.
        """
        pass

    @abstractmethod
    def parent(self, pos: Position) -> Position | None:
        """
        Returns parent if present (or None if at root)
        """
        pass

    @abstractmethod
    def left_child(self, pos: Position) -> Position | None:
        """
        Returns left child if present (otherwise None)
        """
        pass

    @abstractmethod
    def right_child(self, pos: Position) -> Position | None:
        """
        Returns right child if present (otherwise None)
        """
        pass

    @abstractmethod
    def is_root(self, pos: Position) -> bool:
        """
        Returns True if the position is at the root, otherwise False.
        """
        pass

    @abstractmethod
    def is_leaf(self, pos: Position) -> bool:
        """
        Returns True if the position is at a leaf, otherwise False.
        """
        pass

    def get_at(self, pos: Position) -> object:
        """
        Returns the element at given position.
        """
        pass