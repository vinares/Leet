class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        dummy = Node()
        dummy.next = head
        self.DFS_flatten(dummy, head)
        dummy.next.prev = None
        return dummy.next

    def DFS_flatten(self, former: 'Node', latter: 'Node') -> 'Node':
        if not latter: return former
        former.next = latter
        latter.prev = former
        new_latter = latter.next
        tail = self.DFS_flatten(latter, latter.child)
        latter.child = None
        return self.DFS_flatten(tail, new_latter)



