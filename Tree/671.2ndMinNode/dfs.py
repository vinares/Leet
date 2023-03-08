# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ans = -1

        def dfs(nod):
            nonlocal ans
            if not nod: return
            if ans != -1 and nod.val >= ans: return
            if nod.val > root.val: ans = nod.val

            dfs(nod.left)
            dfs(nod.right)

        dfs(root)
        return ans