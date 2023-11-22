# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = []
        def route(stack, root):
            if not root:
                return
            stack.append(root.val)
            if(root.left == None and root.right == None):
                ans.append(int(''.join([str(i) for i in stack])))
            route(stack, root.left)
            route(stack, root.right)
            stack.pop()
            return

        route([],root)
        return sum(ans)

