#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        for i, interval in enumerate(intervals):
            if interval[0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                break
        else:
            intervals.append(newInterval)
        i, j = 0, 1
        while j < len(intervals):
            a, b = intervals[i]
            c, d = intervals[j]
            if b >= c:
                intervals[i] = [a, max(b,d)]
                intervals[j] = None
            else:
                i += 1
                while intervals[i] is None:
                    i += 1
            j += 1
        i = 0
        for j in range(len(intervals)):
            if intervals[j] is not None:
                intervals[i] = intervals[j]
                i += 1
        return intervals[:i]

        

# @lc code=end

