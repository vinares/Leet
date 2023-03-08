#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.cnt = 0
        self.head = head
        node = head
        while node:
            self.cnt += 1
            node = node.next
            

    def getRandom(self) -> int:
        x = randint(1, self.cnt)
        node = self.head
        while x > 1:
            node = node.next
            x -= 1
        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

