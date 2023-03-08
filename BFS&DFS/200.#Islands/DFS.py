class Solution:
    def numIslands(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(x, y):
            nonlocal grid
            grid[x][y] = '0'
            for dire in direction:
                X, Y =  x + dire[0],  y + dire[1]
                if -1 < X < m and -1 < Y < n:
                    if grid[X][Y] == '1':
                        dfs(X,Y)
            return

        ans = 0
        for i in range(m):
            for j in range(n):

                if grid[i][j] == '1':
                    ans += 1
                    dfs(i,j)

        return ans


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


print(Solution().numIslands(grid))