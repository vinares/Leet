#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(s, node):
            if not node:
                return s
            if not node.left and not node.right:
                s.append(node.val)
                return s
            s = dfs(s, node.left)
            s = dfs(s, node.right)
            return s
        
        s1 = dfs([], root1)
        s2 = dfs([], root2)
        return s1 == s2
# @lc code=end

