#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = []
        for interval in sorted(intervals, key=lambda x:x[0]):
            if s and interval[0] <= s[-1][1]:
                s[-1][1] = max(s[-1][1], interval[1])
            else:
                s.append(interval)
        return s

# @lc code=end

