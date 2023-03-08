class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        dummy = Node(0, None, head, None)
        pre = dummy

        stack = []
        stack.append(head)

        while stack:
            cur = stack.pop()

            pre.next = cur
            cur.prev = pre
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
                cur.child = None
            pre = cur

        dummy.next.prev = None
        return dummy.next


