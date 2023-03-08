#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        Expand, Generate = 0, 1
        stack = [(Expand, root)]
        while stack:
            action, node = stack.pop()
            if not node:
                continue
            if action == Expand:
                stack.append((Generate, node))
                stack.append((Expand, node.right))
                stack.append((Expand, node.left))
            else:
                ans.append(node.val)
        return ans

# @lc code=end

