class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m
        dp[0] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[j] = dp[j] + dp[j -1]
        return dp[-1]

print(Solution().uniquePaths(3,2))