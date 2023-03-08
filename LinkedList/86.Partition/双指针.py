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
    def partition(self, head: ListNode, x: int) -> ListNode:
        cur = head
        dummy = ListNode(0, head)
        prev = dummy
        while cur and cur.val < x:
            cur = cur.next
            prev = prev.next
        if not cur: return head
        new = cur.next
        while new:
            if new.val >= x:
                cur = cur.next
                new = new.next
            else:
                tmp = new.next if new.next else None
                new.next = prev.next
                prev.next = new
                prev = new
                cur.next = tmp
                new = tmp
        return dummy.next

case = Solution()
data1 = [1,2,5,4,9,3]
data2 = [1,4,6]
L1 = LinkList().initList(data1)
L2 = LinkList().initList(data2)
l = case.partition(L1, 5)
LinkList().printlist(l)