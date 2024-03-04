#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
from heapq import heapify, heappop, heappush, heappushpop
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h = []
        for num in arr:
            if len(h) < k:
                heappush(h, (-abs(num-x), num))
            elif abs(num-x) < -h[0][0]:
                heappushpop(h, (-abs(num-x), num))
        return sorted([x[1] for x in h])

# @lc code=end

