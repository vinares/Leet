
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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or not k: return  head
        nh = head.next
        nt = head
        cur = head
        count = 1
        while cur.next:
            cur = cur.next
            count += 1
        if k >= count:
            k = count - k % count
        else:
            k = count - k
        while k > 1:
            if nh.next:
                nt = nh
                nh = nh.next
                k -= 1
            else:
                nt = nh
                nh = head
                k -= 1
        if nh == head: return head
        cur = nh
        while cur != nt:
            if cur.next :
                cur = cur.next
            else:
                cur.next = head
                cur = cur.next
        nt.next = None
        return nh




case = Solution()
data1 = [1,2,3,4,5]
data2 = [1,4,6]
L1 = LinkList().initList(data1)
L2 = LinkList().initList(data2)
l = case.rotateRight(L1,7)
LinkList().printlist(l)