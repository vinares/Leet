class Solution:
    def numRollsToTarget(self, n: int, f: int, target: int) -> int:
        dp: list[list]= [[0] * (n + 1) for _ in range(target + 1)]
        for i in range(1, target + 1):
            if i <= f:
                dp[i][1] = 1
            else:
                break

        for j in range(2, n + 1):
            for i in range(j, target + 1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] - dp[i-1-min(i-1,f)][j-1]

        return dp[target][n] % (10 ** 9 + 7)





print(Solution().numRollsToTarget(30,30,500))