#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        q = deque([root])
        while q:
            cur = q.popleft()
            freq[cur.val] += 1
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        ans = []
        maxfreq = 0
        for element, frequency in sorted(freq.items(), key= lambda x:x[1], reverse=True):
            if frequency >= maxfreq:
                maxfreq = frequency
                ans.append(element)
            else:
                break
        return ans


# @lc code=end

