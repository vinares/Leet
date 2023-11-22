from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        q = deque([])
        q.append(root)
        left = True

        def appendnode(q, node):
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        ans = []
        while q:
            cur_level = []
            for i in range(len(q)):
                cur = q.popleft()
                appendnode(q, cur)
                cur_level.append(cur.val)
            if left:
                ans.append(cur_level)
            else:
                ans.append(cur_level[::-1])
            left = not left
        return ans