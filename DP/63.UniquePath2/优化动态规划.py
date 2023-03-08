class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if not m or obstacleGrid[0][0]: return 0
        if m == 1 and n == 1: return 1

        dp = [1 for x in range(n)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[j] = dp[j - 1]
                    continue
                if j == 0:
                    dp[j] = dp[j]
                    continue
                dp[j] += dp[j - 1]
        return dp[-1]


print(Solution().uniquePathsWithObstacles(obstacleGrid= [[0,0],[1,1],[0,0]]))