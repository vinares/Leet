#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
from heapq import heappush, heappushpop, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        h = []
        for num, freq in cnt.items():
            if len(h) < k:
                heappush(h, (freq, num))
            else:
                if h[0][0] < freq:
                    heappushpop(h, (freq, num))
        return [x[1] for x in h]



# @lc code=end

