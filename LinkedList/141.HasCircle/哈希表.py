class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pointer = set()
        while head:
            if head in pointer:
                return True
            else:
                pointer.add(head)
                head = head.next
        return False