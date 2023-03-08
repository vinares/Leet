#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            elif node.left and node.right:
                return min(dfs(node.left), dfs(node.right)) + 1
            elif node.left:
                return dfs(node.left) + 1
            else:
                return dfs(node.right) + 1

        return dfs(root)

# @lc code=end

