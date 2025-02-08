# time to solve 3 mins

# Binary Tree Definition
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#       self.right = right


def dfs(root):
    if not root:
        return 0

    left_height = dfs(root.left)
    right_height = dfs(root.right)

    if left_height == -1 or right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return 1 + max(left_height, right_height)


def solve(root):
    return dfs(root) != -1
