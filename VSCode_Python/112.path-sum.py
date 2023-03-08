#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node, target):
            if target == 0 and not node.left and not node.right:
                return True
            if node.left and dfs(node.left, target-node.left.val):
                return True
            if node.right and dfs(node.right, target-node.right.val):
                return True
            return False
                
        return dfs(root, targetSum-root.val)
# @lc code=end

