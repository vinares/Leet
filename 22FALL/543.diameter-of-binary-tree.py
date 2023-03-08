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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def heightAndDiameter(node):
            if not node:
                return 0
            left_height = heightAndDiameter(node.left)
            right_height = heightAndDiameter(node.right)
            self.ans = max(self.ans, left_height+right_height)
            return max(left_height, right_height) + 1

        heightAndDiameter(root)
        return self.ans


# @lc code=end
