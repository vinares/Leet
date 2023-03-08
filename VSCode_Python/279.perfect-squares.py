#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from math import sqrt
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(sqrt(n)) + 1)]
        dp = [1 if i in squares else 0 for i in range(n+1)]
        possiblesquares = []
        for i in range(1, n+1):
            if dp[i] == 0:
                if not possiblesquares:
                    possiblesquares.append(1)
                elif i-1 in squares:
                    possiblesquares.append(i-1)
                choices = [dp[i-square]+1 for square in possiblesquares]
                dp[i] = min(choices)
        return dp[-1]

# @lc code=end

