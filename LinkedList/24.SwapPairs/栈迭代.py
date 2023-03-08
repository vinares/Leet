class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
            if node.next != None:
                print(node.val, end='->')
            else:
                print(node.val, end='')
            node = node.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tmp = head.next
        A = []
        p = ListNode(None)
        while head and head.next:
            A.append(head)
            A.append(head.next)
            head = head.next.next
            p.next = A.pop()
            p.next.next = A.pop()
            p = p.next.next
        if head:
            p.next = head
        else:
            p.next = None
        return tmp


case = Solution()
data1 = [1,2,3,4,6]
data2 = [1,4,6]
L1 = LinkList().initList(data1)
L2 = LinkList().initList(data2)
l = case.swapPairs(L1)
LinkList().printlist(l)