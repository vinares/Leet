class Solution(object):
    def copyRandomList(self, head):
        if head == None:
            return None
        hp = head
        while hp:
            cur = Node(hp.val, hp.next, hp.random)
            hp.next = cur
            hp = cur.next
        hp = head
        nh = hp.next
        pointer = nh
        while hp:
            pointer.random = pointer.random.next if pointer.random else None
            if pointer.next:
                hp = pointer.next
                pointer = hp.next
            else:
                hp = pointer.next
                pointer = pointer.next
        hp = head
        pointer = head.next
        while pointer.next:
            hp.next = pointer.next
            hp = hp.next
            pointer.next = hp.next
            pointer = pointer.next
        hp.next = None
        pointer.next = None
        return nh



