#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for i in range(m+1)]
        cnt = [(s.count('1'), s.count('0')) for s in strs]
        for one, zero in cnt:
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i-zero][j-one])
        return dp[m][n]

# @lc code=end

