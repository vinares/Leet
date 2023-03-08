# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxAncestorDiff(self, root: [TreeNode]) -> int:
        if not root: return 0

        def dfs(root, maxval, minval):
            if not root: return maxval - minval
            maxval = max(root.val, maxval)
            minval = min(root.val, minval)
            l = dfs(root.left, maxval, minval)
            r = dfs(root.right, maxval, minval)
            return max(l, r)

        return dfs(root, root.val, root.val)
