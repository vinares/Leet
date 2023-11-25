#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = defaultdict(int)
        ps[0] += 1
        ans = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            ans += ps[prefix_sum-k]
            ps[prefix_sum] += 1
        return ans
            

# @lc code=end

