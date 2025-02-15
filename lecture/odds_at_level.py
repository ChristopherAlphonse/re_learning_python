from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while index < len(values):
        current = queue.popleft()
        if values[index] is not None:
            current.left = TreeNode(values[index])
            queue.append(current.left)
        index += 1
        if index < len(values) and values[index] is not None:
            current.right = TreeNode(values[index])
            queue.append(current.right)
        index += 1
    return root


def odds_at_level(node):
    if not node:
        return []
    queue = deque([node])

    result = []

    while queue:
        level_odds = []

        for _ in range(len(queue)):
            current = queue.popleft()

            if current.val % 2 == 1:
                level_odds.append(current.val)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        result.append(level_odds)
    return result


values = [42, 17, 68, 9, 23, 55, 81, 4, 12, None, None, None, 60, None, 95]
root = build_tree(values)
print(odds_at_level(root))
