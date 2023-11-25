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
        parent = collections.deque([root])
        treemap = dict({root:0})
        ans = [[root.val]]

        while parent:
            offset = 1
            ost = -1
            if parent[0].left and treemap[parent[0]] == 0:
                ost = 0
                offset = 2
                ans.insert(0, [])
            ans.append([])
            for i in range(len(parent)):
                cur = parent.popleft()
                if cur.left != None:
                    parent.append(cur.left)
                    treemap[cur.left] = treemap[cur]  + ost
                    ans[treemap[cur.left]].append(cur.left.val)
                if cur.right != None:
                    parent.append(cur.right)
                    treemap[cur.right] = treemap[cur] + offset
                    ans[treemap[cur.right]].append(cur.right.val)
                treemap.pop(cur)
            if len(ans[-1]) == 0: ans.pop()
            print(ans)
        return ans

nums = [3,9,8,4,6,1,7,None,None,None,2,5]
root = Tree().array2tree(nums)
print(Solution().verticalTraverse(root))
