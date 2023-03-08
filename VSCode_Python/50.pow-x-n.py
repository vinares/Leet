#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
from math import log2, floor
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 and x != 0:
            return 1
        ans = 1
        if n < 0:
            x = 1/x
            length = -n//2 + 1
        else:
            length = floor(log2(n)) + 1
        ladder =  [1 for _ in range(length)]
        ladder[0] = x
        for i in range(1, length):
            ladder[i] = ladder[i-1] * ladder[i-1]

        return ans

# @lc code=end

