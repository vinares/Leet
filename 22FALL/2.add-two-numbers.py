#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag = 0
        dummy = ListNode(0, l1)
        prev = l1
        while l1 and l2:
            cur = l1.val + l2.val + flag
            flag = cur // 10
            l1.val = cur % 10
            prev = l1
            l1 = l1.next
            l2 = l2.next
        alive = l1 if l1 else l2
        prev.next = alive
        while alive and flag:
            cur = alive.val + flag
            flag = cur // 10
            prev = alive
            alive.val = cur % 10
            alive = alive.next 
        if flag:
            prev.next = ListNode(1)
        return dummy.next 
# @lc code=end

