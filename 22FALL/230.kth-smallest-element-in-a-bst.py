#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.k = k
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if self.res is not None:
            return
        if not node:
            return
        self.dfs(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.dfs(node.right)

# @lc code=end

