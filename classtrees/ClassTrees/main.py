import random
from binary_tree_abc import BinaryTree, Position
from binary_tree_linked import BinaryTreeLinked

def random_element() -> int:
    """
    Returns a random integer element in the range [1, 10)
    """
    return random.randrange(1, 10)


def random_non_empty_tree() -> BinaryTree:
    """
    Returns a randomly populated binary tree (of a minimum/maximum height).
    """
    def random_extend(tree: BinaryTree, pos: Position, max_height, height):
        if pos is None or height >= max_height:
            return
        if height == 0 or random.random() > 0.7:
            random_extend(tree, tree.add_left_child(pos, random_element()), max_height, height + 1)
        if height == 0 or random.random() > 0.7:
            random_extend(tree, tree.add_right_child(pos, random_element()), max_height, height + 1)

    tree = BinaryTreeLinked()
    tree.add_root(random_element())
    random_extend(tree, tree.root(), 5, 0)
    return tree


def pre_order(tree: BinaryTree, pos: Position, elems: list[object]):
    """
    Traversal of the binary tree, accumulating in a list a pre-order of its elements.
    """
    if pos is None:
        return
    # To do ...
    ...

def post_order(tree: BinaryTree, pos: Position, elems: list[object]):
    """
    Traversal of the binary tree, accumulating in a list a post-order of its elements.
    """
    # To do ...
    ...

def in_order(tree: BinaryTree, pos: Position, elems: list[object]):
    """
    Traversal of the binary tree, accumulating in a list a in-order of its elements.
    """
    # To do ...
    ...

def count(tree: BinaryTree, pos: Position, element: object) -> int:
    """
    Counts how often element occurs in the tree.
    """
    # To do ...
    ...
    return 0

def elements_at_leaves(tree: BinaryTree, pos: Position, elems: list[object]):
    """
    Accumulates the elements at the leaves into a list (left-to-right).
    """
    # To do ...
    ...

random.seed(42)
for _ in range(5):
    print('-------------------------')
    btree = random_non_empty_tree()
    print(btree)
    elements = []
    pre_order(btree, btree.root(), elements)
    print('pre_order =', elements)
    elements.clear()
    post_order(btree, btree.root(), elements)
    print('post_order =', elements)
    elements.clear()
    in_order(btree, btree.root(), elements)
    print('in_order =', elements)
    elements.clear()
    elements_at_leaves(btree, btree.root(), elements)
    print('leaves =', elements)
    print('count(2) =', count(btree, btree.root(), 2))
