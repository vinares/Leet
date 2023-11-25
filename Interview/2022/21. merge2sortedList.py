# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        if not l1: return l2
        if not l2: return l1
        dummy = ListNode()
        dummy.next = l1 if l1.val <= l2.val else l2

        while l1 and l2:
            if l1.val <= l2.val and l1.next and l1.next.val <= l2.val:
                l1 = l1.next
            elif l1.val > l2.val and l2.next and l2.next.val < l1.val:
                l2 = l2.next
            else:
                if l1.val <= l2.val:
                    tmp = l1.next
                    l1.next = l2
                    l1 = tmp
                else:
                    tmp = l2.next
                    l2.next = l1
                    l2 = tmp
        return dummy.next