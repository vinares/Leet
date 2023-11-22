import collections

class Node:
    # Initialize the attributes of Node
    def __init__(self, data):
        self.left = None # Left Child
        self.right = None # Right Child
        self.val = data # Node Data

class Tree:
    def array2tree(self, nums):
        n = len(nums)
        if n == 0: return Node()
        root = Node(nums[0])
        q = collections.deque([root])
        i = 1
        while(q and i < n):
            cur = q[0]
            if nums[i] == None:
                i += 1
                continue
            new_node = Node(nums[i])
            if cur.left == None:
                i += 1
                cur.left = new_node
                if new_node:
                    q.append(new_node)
            if i == n: break
            new_node = Node(nums[i]) if nums[i] else None
            if cur.right == None:
                i += 1
                cur.right = new_node
                if new_node:
                    q.append(new_node)
                q.popleft()

        return root

class Solution:
    def verticalTraverse(self, root):
        ans = []
        treemap = collections.defaultdict(list)
        q = collections.deque([])
        q.append((root, 0, 0))

        while q:
            childs = []
            while q:
                node, row, col = q.popleft()
                if q and q[0][2] == col:
                    newnode, _, _ = q.popleft()
                    q.insert(0,(node, row, col))
                    node = newnode
                treemap[col].append(node.val)
                if node.left:
                    childs.append((node.left, row + 1, col - 1))
                if node.right:
                    childs.append((node.right, row + 1, col + 1))
            q = collections.deque(childs)
        for key, val in sorted(treemap.items()):
            if val:
                ans.append([])
                for i in range(len(val)):
                    ans[-1].append(val[i])
        return ans


nums = [3,9,8,4,6,1,7,None,None,None,2,5]
root = Tree().array2tree(nums)
print(Solution().verticalTraverse(root))
