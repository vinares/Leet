class Solution:
    def minPathSum(self, grid: list) -> int:
        if not grid[0]:return 0
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        print(dp)
        return  dp[m - 1][n - 1]

print(Solution().minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))