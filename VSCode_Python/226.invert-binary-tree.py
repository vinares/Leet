#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node or (not node.left and not node.right):
                return
            elif not node.left:
                node.left = node.right
                node.right = None
                dfs(node.left)
            elif not node.right:
                node.right = node.left
                node.left = None
                dfs(node.right)
            else:
                node.left, node.right = node.right, node.left
                dfs(node.left)
                dfs(node.right)
            return
        dfs(root)
        return root
# @lc code=end

