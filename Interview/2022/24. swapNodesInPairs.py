# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while head and head.next:
            new_head = head.next.next
            prev.next = head.next
            prev = head
            head.next.next = head
            head.next = new_head

            head = new_head
        return dummy.next
