# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.node2pa = dict()

    def buildPath(self, p, q, root):
        stack = [root]
        while stack and not (p in self.node2pa and q in self.node2pa):
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
                self.node2pa[cur.left] = cur
            if cur.right:
                stack.append(cur.right)
                self.node2pa[cur.right] = cur

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.buildPath(p, q, root)
        P2root = []
        while p != root:
            P2root.append(p)
            p = self.node2pa[p]
        P2root.append(root)

        while q != root and q not in P2root:
            q = self.node2pa[q]

        return q