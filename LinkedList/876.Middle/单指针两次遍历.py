# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data) -> ListNode:
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node   #连线
            p = p.next      #移位
        return r

    def printlist(self, head):
        if head == None: return
        node = head
        while node != None:
            print(node.val, end=' ')
            node = node.next

class Solution:
    def middleNode(self, head: ListNode) :
        n, cur = 1, head
        while cur.next != None:
            n += 1
            cur = cur.next
        cur = head
        for i in range(n//2):
            cur = cur.next
        return cur.val



case = Solution()
L = LinkList()
data = [1,2,3,4,5]
head = L.initList(data)
print(case.middleNode(head))