#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(x * y for x, y in sorted(Counter(s).items(), key=lambda x: (x[1], x[0]), reverse=True))
# @lc code=end
