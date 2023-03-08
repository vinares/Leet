#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        infinity = 10 ** 9
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1, 0, -1):
            for j in range(i+1, n+1):
                dp[i][j] = j + dp[i][j-1]
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], k+max(dp[i][k-1], dp[k+1][j]))
        return dp[1][n]


# @lc code=end

