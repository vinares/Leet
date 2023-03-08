#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        all_nodes = []
        q = [(0, 0, root)]
        while q:
            new_q = []
            for col, row, node in q:
                all_nodes.append((col, row, node.val))
                if node.left:
                    new_q.append((col-1, row+1, node.left))
                if node.right:
                    new_q.append((col+1, row+1, node.right))
            q = new_q
        all_nodes.sort()
        cur_col = 1
        result = []
        for col, row, value in all_nodes:
            if col != cur_col:
                cur_col = col
                result.append([])
            result[-1].append(value)
        return result


# @lc code=end

