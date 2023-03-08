#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def backtrack(node, cur):
            if not node:
                return 0
            ret = 0
            cur += node.val
            ret += prefix_sum[cur-targetSum]
            prefix_sum[cur] += 1
            ret += backtrack(node.left, cur)
            ret += backtrack(node.right, cur)
            prefix_sum[cur] -= 1
            return ret

        return  backtrack(root, 0)     

# @lc code=end

