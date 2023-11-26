#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from collections import OrderedDict

class DoubleLinkedList():
    def __init__(self, key=None, val=None, next=None, prev=None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class orderedDict():
    def __init__(self) -> None:
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList(None, None, None, self.head)
        self.head.next = self.tail
        self.dictionary = {}
        

    def add_to_head(self, key, val):
        node = DoubleLinkedList(key, val)
        self.dictionary[key] = node
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
    
    def remove_tail_node(self):
        last_node = self.tail.prev
        if last_node != self.head:
            prev_node = last_node.prev
            prev_node.next = self.tail
            self.tail.prev = prev_node
            self.dictionary.pop(last_node.key)
            del last_node

    def get(self, key):
        ans = -1
        if key in self.dictionary:
            node = self.dictionary[key]
            ans = node.val
            self.move_to_head(key)
        return ans
    
    def update(self, key, val=None):
        if key not in self.dictionary:
            node = DoubleLinkedList(key, val)
            self.dictionary[key] = node
        else:
            node =  self.dictionary[key]
            if val is not None:
                node.val = val
        self.move_to_head(key)

    def move_to_head(self, key):
        node = self.dictionary[key]
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
        
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity
        """
        self.od = orderedDict()
        """

    def get(self, key: int) -> int:
        # return self.od.get(key)
        if key in self:
            self.move_to_end(key)
            return self[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        self.od.update(key, value)
        if len(self.od.dictionary) > self.capacity:
            self.od.remove_tail_node()
        """
        if key in self:
            self.move_to_end(key)
        self[key] =  value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

