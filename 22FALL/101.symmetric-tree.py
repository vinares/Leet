#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left, right = deque([root]), deque([root])
        while left and right:
            new_left, new_right = [], []
            while left and right:
                cur_left, cur_right = left.popleft(), right.popleft()
                if not cur_right and not cur_left:
                    continue
                if not cur_left or not cur_right:
                    return False
                if cur_left.val != cur_right.val:
                    return False
                new_left.append(cur_left.left)
                new_left.append(cur_left.right)
                new_right.append(cur_right.right)
                new_right.append(cur_right.left)
            if left or right:
                return False
            left, right = deque(new_left), deque(new_right)
        return True

        

    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
    def compare(self, left, right):
        if not left or not right:
            return left == right
        return left.val == right.val and (self.compare(left.left, right.right)) and self.compare(left.right, right.left)
    """


# @lc code=end

