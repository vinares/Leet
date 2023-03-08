"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = deque()
        q.append(root)
        
        while q:
            n = len(q)
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
                q.append(cur.right)
                
            for i in range(n - 1):
                _next = q.popleft()
                if _next.left:
                    q.append(_next.left)
                    q.append(_next.right)
                cur.next = _next
                cur = _next
            cur.next = None
        return root