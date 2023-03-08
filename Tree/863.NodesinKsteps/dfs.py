# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        father = defaultdict(TreeNode)
        father[root] = None

        def findTarget(nod):
            nonlocal father
            if not nod: return
            if nod.val == target:
                return

            if nod.left:
                father[nod.left] = nod
            if nod.right:
                father[nod.right] = nod

            findTarget(nod.left)
            findTarget(nod.right)
            return

        findTarget(root)

        def dfs(nod, k, prev):

            if not nod:return
            if k == 0:
                ans.append(nod)
                return
            if nod.left and nod.left != prev:dfs(nod.left, k - 1, nod)
            if nod.right and nod.right != prev:dfs(nod.right,k - 1, nod)
            if nod in father and nod[father] != prev:
                dfs(father[nod], k - 1, nod)
        dfs(target, k, target)
        return ans
