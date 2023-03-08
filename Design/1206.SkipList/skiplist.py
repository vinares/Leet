import random
class SkipNode:
    def __init__(self, val= -1, right= None, down= None):
        self.val = val
        self.right = right
        self.down = down

class Skiplist:

    def __init__(self):
        self.head = SkipNode()

    def search(self, target: int) -> bool:
        node = self.head
        while node:
            while node.right and node.right.val < target:
                node = node.right
            if node.right and node.right.val == target:
                return True
            node = node.down
        return False

    def add(self, num: int) -> None:
        nodes = []
        node = self.head
        while node:
            while node.right and node.right.val < num:
                node = node.right
            nodes.append(node)
            node = node.down
        insert = True
        down = None
        while nodes and insert:
            prev = nodes.pop()
            node = SkipNode(num, prev.right, down)
            prev.right = node
            insert = (random.randint(0, 1) == 0)
            #insert = *random.getrandbits(1) == 0)
            down = node
        if insert:
            self.head = SkipNode(-1, None, self.head)

    def erase(self, num: int) -> bool:
        node = self.head
        found = False
        while node:
            while node.right and node.right.val < num:
                node = node.right
            if node.right and node.right.val == num:
                node.right = node.right.right
                found = True
            node = node.down
        return found

skiplist = [30,40,50,60,70,90]
Answer = Skiplist()
for x in skiplist:
    Answer.add(x)
print(Answer.add(55))
print(Answer.search(55))
print(Answer.erase(55))
