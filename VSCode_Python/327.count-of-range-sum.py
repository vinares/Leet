#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#

# @lc code=start
from bisect import bisect_left, bisect_right, insort
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        s, ans = 0, 0
        sorted_sum = [0]
        for num in nums:
            s += num
            l = bisect_left(sorted_sum, s-upper)
            r = bisect_right(sorted_sum, s-lower)
            ans += r-l
            insort(sorted_sum, s)
        return ans


# @lc code=end

