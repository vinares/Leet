#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateSubTrees(start, end):
            if start > end:
                return [None]
            allTrees = []
            for pivot in range(start, end+1):
                leftTrees = generateSubTrees(start, pivot-1)
                rightTrees = generateSubTrees(pivot+1, end)
                for l in leftTrees:
                    for r in rightTrees:
                        curTree = TreeNode(pivot)
                        curTree.left = l
                        curTree.right = r
                        allTrees.append(curTree)
            return allTrees
        return generateSubTrees(1, n) if n > 0 else []


# @lc code=end

