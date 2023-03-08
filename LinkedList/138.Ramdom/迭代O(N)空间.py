class Solution(object):
    """
    :type head: Node
    :rtype: Node
    """
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visited = {}
    def clone(self, head):
        if head:
            if head in self.visited:
                return self.visited[head]
            else:
                node = Node(head.val, None, None)
                self.visited[head] = node
                return node
        return None
    def copyRandomList(self, head):
        if head == None:
            return None
        old_h = head
        new_h = Node(head.val, None, None)
        self.visited[head] = new_h
        pointer = new_h
        while old_h:
            pointer.random = self.clone(old_h.random)
            pointer.next  =self.clone(old_h.next)
            old_h = old_h.next
            pointer = pointer.next
        return self.visited[head]


