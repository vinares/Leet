#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * n
        for i in range(n):
            if s[i] != '0':
                dp[i+1] += dp[i]
            if i>=1 and s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
        return dp[n]
 
 # @lc code=end

