#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def dfs(node, tmp):
            if not node.left and not node.right:
                return [tmp+str(node.val)]
            total = []
            if node.left:
                total.extend(dfs(node.left, tmp+str(node.val)))
            if node.right:
                total.extend(dfs(node.right, tmp+str(node.val)))
            return total
        
        return sum([int(num) for num in dfs(root, '')])
            
# @lc code=end

