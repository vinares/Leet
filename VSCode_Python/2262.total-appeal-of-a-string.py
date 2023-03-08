#
# @lc app=leetcode id=2262 lang=python3
#
# [2262] Total Appeal of A String
#

# @lc code=start
class Solution:
    def appealSum(self, s: str) -> int:
        mem  = dict()
        prev = 0
        cur = 0
        res = 0
        for i, x in enumerate(s):
            if x in mem:
                cur = prev + i  - mem[x]
            else:
                cur = prev + i + 1
            mem[x] = i
            prev = cur
            res += prev
        return res
# @lc code=end

