
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data) -> ListNode:
        # 创建头结点
        if not data:
            return self.head
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


class Solution(object):
    def mergeKLists(self, lists: list) -> ListNode:
        if not lists: return
        n = len(lists)

        def merge(left: ListNode, right: ListNode):
            if not (left and right):
                return left if left else right
            if left.val <= right.val:
                left.next = merge(left.next, right)
                return left
            else:
                right.next = merge(left,right.next)
                return right
        def divide(begin,end):
            if begin == end:
                return lists[begin]
            mid = begin + (end - begin)//2
            left = divide(begin, mid)
            right = divide(mid + 1, end)
            return merge(left, right)

        return divide(0, n - 1)


case = Solution()
data1 = [1,2,3,4,5,9]
data2 = [6]
data3 = [2,4,4,7]
L1 = LinkList().initList(data1)
L2 = LinkList().initList(data2)
L3 = LinkList().initList(data3)
L = [L1,L2,L3]
l = case.mergeKLists(L)
LinkList().printlist(l)