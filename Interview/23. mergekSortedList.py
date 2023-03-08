# Definition for singly-linked list.
import sys


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:

    def mergeKLists(self, lists):
        def divideAndConquer(lists):
            n = len(lists)
            if n == 0:
                return None
            elif n == 1:
                return lists[0]
            elif n == 2:
                l1, l2 = lists[0], lists[1]
                if not l1: return l2
                if not l2: return l1

                dummy = ListNode()
                dummy.next = l1 if l1.val <= l2.val else l2

                while l1 and l2:
                    if l1.val <= l2.val and l1.next and l1.next.val <= l2.val:
                        l1 = l1.next
                    elif l1.val > l2.val and l2.next and l2.next.val < l1.val:
                        l2 = l2.next
                    else:
                        if l1.val <= l2.val:
                            tmp = l1.next
                            l1.next = l2
                            l1 = tmp
                        else:
                            tmp = l2.next
                            l2.next = l1
                            l2 = tmp
                return dummy.next
            else:
                left, right = divideAndConquer(lists[0:n // 2]), divideAndConquer(lists[n // 2::])
                return divideAndConquer([left, right])

        return divideAndConquer(lists)
    def hashtable(self, lists):

        head = ListNode()
        cur = head
        q = dict()
        for node in lists:
            if node:
                q[node] = node.val
        while q:
            key, val = sorted(q.items(), key=lambda x:x[1],reverse=False)[0]
            cur.next = key
            q.pop(key)
            cur = cur.next
            if cur.next:
                q[cur.next] = cur.next.val
        return head
    def priorityQueue(self, lists):
        import heapq
        head = cur = ListNode()
        q = []
        heapq.heapify(q)
        cnt = 0
        for node in lists:
            if node:
                cnt += 1
                heapq.heappush(q, (node.val, cnt, node))

        while q:
            _, t, cur.next = heapq.heappop(q)
            cur = cur.next
            if cur.next:
                heapq.heappush(q,(cur.next.val, t, cur.next))

        return head.next

    def constantSpace(self, lists):
        if not lists: return

        dummy = ListNode(sys.maxsize)
        cur = dummy
        empty = False
        minimal, index = dummy, -1

        while not empty:
            empty = True
            for i, node in enumerate(lists):
                if node:
                    empty = False
                    if node.val < minimal.val:
                        minival, index = node, i

            if not empty:
                cur.next = minival
                cur = cur.next
                if cur.next:
                    lists[index] = cur.next
                else:
                    lists[index], lists[-1] = lists[-1], lists[index]
                    lists.pop()
        return dummy.next

    def arraymerge(self, lists):
        if not lists:
            return []
        pointers = [0 for _ in range(len(lists))]
        ans = []

        empty = False
        cur, i = lists[0][0], 0

        while not empty:
            empty = True
            for j in range(len(lists)):
                if pointers[j] < len(lists[j]):
                    empty = False
                    if lists[j][pointers[j]] < cur:
                        cur = lists[j][pointers[j]]
                        i = j
            if empty: break
            ans.append(cur)
            pointers[i] += 1
            cur = 2 ** 31
        return ans


print(Solution().arraymerge([[1,2,3],[2,3,4],[-1, 3, 10]]))