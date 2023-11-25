#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        dummy = head
        while head:
            node = Node(head.val, head.next, None)
            head.next = node
            head = node.next
        
        head = dummy
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next
        
        head = dummy
        new_head = dummy.next
        while head:
            node = head.next
            head.next = node.next
            head = head.next
            if head:
                node.next = head.next
        return new_head

# @lc code=end

