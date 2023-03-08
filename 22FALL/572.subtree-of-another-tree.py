#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        def check(node, subnode):
            if node == subnode:
                return True
            if not node or not subnode:
                return False
            return node.val == subnode.val and check(node.left, subnode.left) and check(node.right, subnode.right)
        
        def dfs(node):
            if not node:
                return False
            if check(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)

# @lc code=end

