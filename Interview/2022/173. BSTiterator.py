# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.stack.append(root)
        self._left()

    def next(self) -> int:
        cur = self.stack.pop()
        if cur.right:
            self.stack.append(cur.right)
            self._left()
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _left(self):
        while self.stack[-1].left:
            self.stack.append(self.stack[-1].left)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()