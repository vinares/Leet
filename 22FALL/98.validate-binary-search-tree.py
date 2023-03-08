#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        flag = True
        if root.left:
            flag = flag and root.left.val < root.val and self.isValidBST(root.left)
        if root.right:
            flag = flag and root.right.val > root.val and self.isValidBST(root.right)
        return flag
        
# @lc code=end

