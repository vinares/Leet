#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root or root.val == x or root.val == y:
            return False
        q = [(root, None)]

        while q:
            new_q = []
            X, Y = None, None
            for node, _ in q:
                if node.left:
                    new_q.append((node.left, node))
                    if node.left.val == x:
                        X = new_q[-1]
                    if node.left.val == y:
                        Y = new_q[-1]
                    
                if node.right:
                    new_q.append((node.right, node))
                    if node.right.val == x:
                        X = new_q[-1]
                    if node.right.val == y:
                        Y = new_q[-1]
            if X and Y:
                if X[1] == Y[1]:
                    return False
                return True
            elif not X and not Y:
                q = new_q
                continue
            else:
                return False
        return False

# @lc code=end

