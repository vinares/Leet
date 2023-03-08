#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balance(node):
            if not node:
                return 0
            lh = balance(node.left)
            rh = balance(node.right)
            
            if abs(lh-rh) > 1 or lh == -1 or rh == -1:
                return -1
            return max(lh, rh) + 1
        return True if balance(root) > -1 else False

# @lc code=end

