#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        mem = {}
        h = []
        for i, node in enumerate(lists):
            if not node: continue
            h.append((node.val, i))
            mem[i] = node
        if not h: return None
        heapify(h)    
        _, head_index = heappop(h)
        head = mem[head_index]
        if head.next:
            heappush(h, (head.next.val, head_index))
            mem[head_index] = head.next
        else:
            mem.pop(head_index)
        dummy = head
        while h:
            val, index = heappop(h)
            node = mem[index]
            head.next = node
            head = node
            if node.next:
                mem[index] = node.next
                heappush(h, (head.next.val, index))
            else:
                mem.pop(index)
        return dummy


# @lc code=end

