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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            s += a + b
            p.next = ListNode(s % 10)   #分配并连线
            p = p.next                  #移位
            s = s // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next

case = Solution()
data1 = [2,4,3]
data2 = [5,6,4]
L1 = LinkList().initList(data1)
L2 = LinkList().initList(data2)
l = case.addTwoNumbers(L1, L2)
LinkList().printlist(l)