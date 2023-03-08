#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        Expand, Generate = 0, 1
        stack = [(Expand, root)]
        while stack:
            action, node = stack.pop()
            if node is None:
                continue
            if action == Expand:
                stack.append((Expand, node.right))
                stack.append((Expand, node.left))
                stack.append((Generate, node))
            else:
                ans.append(node.val)
        return ans

# @lc code=end

