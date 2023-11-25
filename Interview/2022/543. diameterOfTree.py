# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def dfs(root, depth):
            if not root: return depth - 1, 0
            if not root.left and not root.right: return depth, 0

            ld, lm = dfs(root.left, depth + 1)
            rd, rm = dfs(root.right, depth + 1)

            length = ld + rd - depth * 2

            return max(ld, rd), max([lm, rm, length])

        d, a = dfs(root, 0)

        return a