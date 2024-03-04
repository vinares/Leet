#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        val_to_new = dict()
        val_to_new[node.val] = Node(node.val)

        q = deque([node])
        while q:
            cur = q.popleft()
            cur_new = val_to_new[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in val_to_new:
                    val_to_new[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                cur_new.neighbors.append(val_to_new[neighbor.val])
        return val_to_new[node.val]
                



# @lc code=end

