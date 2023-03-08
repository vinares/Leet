#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sorted(Counter(nums).items(), key= lambda x: x[1], reverse=False)[0][0]
# @lc code=end

