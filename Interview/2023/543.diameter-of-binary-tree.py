#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_depth(self, root):
        if not root:
            return 0
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        self.diameter = max(self.diameter, left+right)
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        self.get_depth(root)
        return self.diameter

# @lc code=end

