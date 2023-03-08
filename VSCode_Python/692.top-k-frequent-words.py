#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]), reverse=False)[i][0] for i in range(k)]
# @lc code=end

