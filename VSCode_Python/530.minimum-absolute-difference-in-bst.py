#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def dfs(minimum, parents):
            node = parents[-1]
            if not node.left and not node.right:
                return minimum
            if node.left:
                for parent in parents:
                    minimum = min(minimum, abs(parent.val - node.left.val))
                minimum = min(minimum, dfs(minimum, parents+[node.left]))
            if node.right:
                for parent in parents:
                    minimum = min(minimum, abs(parent.val - node.right.val))
                minimum = min(minimum, dfs(minimum, parents+[node.right]))
            return minimum
        return dfs(10 ** 9, [root])
# @lc code=end

