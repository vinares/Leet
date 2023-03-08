class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if not m or obstacleGrid[0][0]: return 0
        if m == 1 and n == 1: return 1
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i ==0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j - 1]
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                if i and j:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[m-1][n-1]



print(Solution().uniquePathsWithObstacles(obstacleGrid= [[0,0],[1,1],[0,0]]))