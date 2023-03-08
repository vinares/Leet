#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)
        return [cnt[i][0] for i in range(k)]
# @lc code=end

