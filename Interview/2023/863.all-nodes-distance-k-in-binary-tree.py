#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def mark_p(node):
            if not node.left and not node.right:
                return
            if node.left:
                parent[node.left] = node
                mark_p(node.left)
            if node.right:
                parent[node.right] = node
                mark_p(node.right)
            return

        mark_p(root)
        q = [target]
        visited = set()
        visited.add(target)
        cur = 0
        while q:
            nq = []
            if cur == k:
                break
            for node in q:
                if node.left and node.left not in visited:
                    nq.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    nq.append(node.right)
                    visited.add(node.right)
                if node in parent and parent[node] not in visited:
                    nq.append(parent[node])
                    visited.add(parent[node])
            q = nq                
            cur += 1                
        return [node.val for node in q]

# @lc code=end

