#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        q = deque([root])
        flag = False
        while q:
            cur = q.popleft()
            if cur.left:
                if flag:
                    return False
                q.append(cur.left)
            else:
                flag = True
            if cur.right:
                if flag:
                    return False
                q.append(cur.right)
            else:
                flag = True
        return True
            
# @lc code=end

