class Solution:
    def minPathSum(self, grid: list) -> int:
        if not grid[0]:return 0
        m, n = len(grid), len(grid[0])
        queue = set((0,0,grid[0][0]))

        while queue:
            new_queue = set()
            for x,y,z in queue:
                xx = z + grid[x + 1][y] if x + 1 < m else float('inf')
                yy = z + grid[x][y + 1] if y + 1 < n else float('inf')

        def

print(Solution().minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))