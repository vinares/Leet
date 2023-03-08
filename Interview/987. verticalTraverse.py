# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root:[TreeNode]) -> list:
        q = deque()
        q.append((root, 0, 0))
        answer = defaultdict(list)

        while q:
            node, row, col = q.popleft()
            answer[col].append((row, node.val))
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))

        ans = []
        for _, vertical in answer.items():
            vertical = sorted(vertical)
            ans.append([value for a, value in vertical])
        return ans