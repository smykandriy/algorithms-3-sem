class BinaryTree:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def check_balance_and_height(node: BinaryTree) -> tuple[bool, int]:
    if node is None:
        return True, 0

    is_left_balanced, left_height = check_balance_and_height(node.left)
    is_right_balanced, right_height = check_balance_and_height(node.right)

    height = max(left_height, right_height) + 1
    is_balanced = is_left_balanced and is_right_balanced and abs(left_height - right_height) <= 1

    return is_balanced, height


def is_tree_balanced(node: BinaryTree) -> bool:
    balanced, _ = check_balance_and_height(node)
    return balanced
