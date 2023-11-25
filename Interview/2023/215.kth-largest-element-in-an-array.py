#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from heapq import heapify, nlargest, heappop, heappushpop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapify(h)
        for i in range(k, len(nums)):
            if nums[i] > h[0]:
                heappushpop(h, nums[i])
        return heappop(h)

# @lc code=end

