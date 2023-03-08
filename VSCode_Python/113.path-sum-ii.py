#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.ans = []

        def bfs(tmp, target, node):
            if target==0 and not node.right and not node.left:
                self.ans.append(tmp)
            if node.left:
                bfs(tmp+[node.left.val], target-node.left.val, node.left)
            if node.right:
                bfs(tmp+[node.right.val], target-node.right.val, node.right)
            return
        bfs([root.val], targetSum-root.val, root)
        return self.ans
# @lc code=end

