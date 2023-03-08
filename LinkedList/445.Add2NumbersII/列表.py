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
        L1, L2 = [], []
        while l1:
            L1.append(l1.val)
            l1 = l1.next
        while l2:
            L2.append(l2.val)
            l2 = l2.next
        rst = None
        s = 0
        while L1 or L2 or s:
            a = 0 if not L1 else L1.pop()
            b = 0 if not L2 else L2.pop()
            s += a + b
            p = ListNode(s % 10)    #分配
            p.next = rst            #连线
            rst = p                 #向前移位
            s = s // 10
        return rst
case = Solution()
data1 = [9,1]
data2 = [4,6,1]
L1 = LinkList().initList(data1)
L2 = LinkList().initList(data2)
l = case.addTwoNumbers(L1, L2)
LinkList().printlist(l)