import unittest

from algorithms import BinaryTree, is_tree_balanced

balanced_tree = BinaryTree(5)
balanced_tree.left = BinaryTree(4)
balanced_tree.right = BinaryTree(7)
balanced_tree.right.right = BinaryTree(8)

unbalanced_tree = BinaryTree(5)
unbalanced_tree.left = BinaryTree(4)
unbalanced_tree.right = BinaryTree(7)
unbalanced_tree.right.right = BinaryTree(8)
unbalanced_tree.right.right.right = BinaryTree(9)


class TestBalancedTree(unittest.TestCase):
    def test_balanced_tree(self):
        expected_result = True
        actual_result = is_tree_balanced(balanced_tree)
        self.assertEqual(expected_result, actual_result)

    def test_unbalanced_tree(self):
        expected_result = False
        actual_result = is_tree_balanced(unbalanced_tree)
        self.assertEqual(expected_result, actual_result)
