#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def in_order_rev(node, cur_sum):
            if not node:
                return cur_sum
            cur_sum = in_order_rev(node.right, cur_sum)
            cur_sum += node.val
            node.val = cur_sum
            cur_sum = in_order_rev(node.left, cur_sum)
            return cur_sum
        
        in_order_rev(root, 0)
        return root

# @lc code=end

