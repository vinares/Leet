#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([(root, '0b'+str(root.val))])
        while q:
            cur, bin_str = q.popleft()
            if not cur.left and not cur.right:
                res += int(bin_str, 2)
                continue
            if cur.left:
                q.append((cur.left, bin_str+str(cur.left.val)))
            if cur.right:
                q.append((cur.right, bin_str+str(cur.right.val)))
        return res

# @lc code=end

