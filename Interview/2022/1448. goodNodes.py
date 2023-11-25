# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        if not root: return ans

        def dfs(root, ever):
            nonlocal ans
            if not root: return
            if root.val < ever:
                dfs(root.left, ever)
                dfs(root.right, ever)
                return
            else:
                ans += 1
                ever = max(ever, root.val)
                dfs(root.left, ever)
                dfs(root.right, ever)
                return

        dfs(root, - 10 ** 4 - 1)
        return ans