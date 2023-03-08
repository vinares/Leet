#
# @lc app=leetcode id=1039 lang=python3
#
# [1039] Minimum Score Triangulation of Polygon
#

# @lc code=start

from functools import lru_cache
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def backtrack(left, right):
            if right - left + 1 < 3:
                return 0
            answer = 10 ** 9
            for k in range(left+1, right):
                answer = min(answer, values[k]*values[left]*values[right] + backtrack(left, k) + backtrack(k, right))
            return answer
        return backtrack(0, len(values)-1)
# @lc code=end

