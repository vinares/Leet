#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations):
        n = len(citations)
        cnt = [0] * (n+1)
        for cite in citations:
            cnt[min(n, cite)] += 1
        accum = list(accumulate(cnt[1:][::-1]))[::-1]
        res = [accum[i] >= i+1 for i in range(n)] + [0]
        return res.index(0)
# @lc code=end

