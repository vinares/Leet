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
        num1 = Solution().LLtoInt(l1)
        num2 = Solution().LLtoInt(l2)
        num = num1 + num2
        NUM = str(num)
        print(NUM)
        node = ListNode(NUM[0])
        for i in range(1,len(NUM)):
            node = ListNode(NUM[i],node)
        return node

    def LLtoInt(self, l: ListNode) -> int:
        i, num = 0, 0
        while l:
            num += l.val*(10**i)
            l = l.next
            i += 1
        return num


case = Solution()
data1 = [9,1]
data2 = [1,6,1]
L1 = LinkList().initList(data1)
L2 = LinkList().initList(data2)
l = case.addTwoNumbers(L1, L2)
LinkList().printlist(l)