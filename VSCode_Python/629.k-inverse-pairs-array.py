#
# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#

# @lc code=start
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [1] + [0 for _ in range(k)]
        for i in range(2, n+1):
            tmp = [1] + [0 for _ in range(k)]
            for j in range(1, k+1):
                if j > i * (i-1)//2:
                    break
                tmp[j] = tmp[j - 1] + dp[j]
                if j >= i:
                    tmp[j] -= dp[j - i]
            dp = tmp
        return dp[-1] % (10 ** 9 + 7)
# @lc code=end

