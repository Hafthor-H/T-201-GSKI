from binary_tree_abc import Position, BinaryTree

class BinaryTreeLinked(BinaryTree):

    ##############################################################################
    # Private helper classes and methods.
    ##############################################################################
    class _Node:
        def __init__(self, parent, element, left, right):
            self.parent = parent
            self.element = element
            self.left = None
            self.right = None

    def _validate_pos(self, pos: Position):
        if pos is None or pos.handle is None:
            raise IndexError('Invalid position')

    def _representation(self, node: _Node) -> str:
        if node is None:
            return "-"
        l = self._representation(node.left)
        r = self._representation(node.right)
        return '(' + str(node.element) + ' ' + l + ' ' + r + ')'

    ##############################################################################
    # Public methods (implementing the BinaryTree Abstract Base Class interface).
    ##############################################################################

    def __init__(self):
        self._root = None

    def __str__(self):
        return self._representation(self._root)

    def clear(self):
        self._root = None

    def add_root(self, element: object) -> Position:
        node = self._Node(None, element, None, None)
        self._root = node
        return Position(node)

    def add_left_child(self, pos: Position, element: object) -> Position:
        # To do ...
        pass

    def add_right_child(self, pos: Position, element: object) -> Position:
        # To do ...
        ...

    def remove_subtree(self, pos: Position):
        # To do. Hint: think recursively!
        ...

    def remove(self, pos: Position):
        self._validate_pos(pos)
        if not self.is_leaf(pos):
            raise IndexError('remove a non-leaf')
        # To do
        ...

    def replace(self, pos: Position, element: object) -> object:
        # To do
        ...

    def is_empty(self) -> bool:
        # To do
        ...

    def root(self) -> Position | None:
        return Position(self._root) if self._root is not None else None

    def parent(self, pos: Position) -> Position | None:
        self._validate_pos(pos)
        curr = pos.handle
        node = curr.parent
        return Position(node) if node is not None else None

    def left_child(self, pos: Position) -> Position | None:
        self._validate_pos(pos)
        curr = pos.handle
        node = curr.left
        return Position(node) if node is not None else None

    def right_child(self, pos: Position) -> Position:
        self._validate_pos(pos)
        curr = pos.handle
        node = curr.right
        return Position(node) if node is not None else None

    def is_root(self, pos: Position) -> bool:
        self._validate_pos(pos)
        curr = pos.handle
        return curr.parent is None

    def is_leaf(self, pos: Position) -> bool:
        self._validate_pos(pos)
        curr = pos.handle
        return curr.left is None and curr.right is None

    def get_at(self, pos: Position) -> object:
        self._validate_pos(pos)
        curr = pos.handle
        return curr.element
