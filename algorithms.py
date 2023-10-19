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


def get_tree_diameter(node: BinaryTree) -> int:
    if node is None:
        return 0

    _, left_height = check_balance_and_height(node.left)
    _, right_height = check_balance_and_height(node.right)

    left_diameter = get_tree_diameter(node.left)
    right_diameter = get_tree_diameter(node.right)

    max_diameter = max(max(left_diameter, right_diameter), left_height + right_height)

    return max_diameter


def check_tree_balance_with_stack(node: BinaryTree) -> bool:
    if node is None:
        return True

    stack = [(node, 0)]

    while stack:
        current_node, height = stack.pop()

        left_height = right_height = 0

        if current_node.left:
            stack.append((current_node.left, height + 1))
            left_height = height + 1
        if current_node.right:
            stack.append((current_node.right, right_height))
            right_height = height + 1

        if abs(left_height - right_height) > 1:
            return False

    return True


root = BinaryTree(50)
v17 = root.left = BinaryTree(17)
v9 = v17.left = BinaryTree(9)
v14 = v9.right = BinaryTree(14)
v12 = v14.left = BinaryTree(12)
v23 = v17.right = BinaryTree(23)
v19 = v23.left = BinaryTree(19)
v76 = root.right = BinaryTree(76)
v54 = v76.left = BinaryTree(54)
v72 = v54.right = BinaryTree(72)
v67 = v72.left = BinaryTree(67)
