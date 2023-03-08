#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        eswn = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def submerge_island(x, y):
            lands = deque([(x, y)])
            while lands:
                i, j = lands.popleft()            
                for dx, dy in eswn:
                    if 0 <= i+dx < m and 0 <= j+dy < n and grid[i+dx][j+dy] == '1':
                        grid[i+dx][j+dy] = '0'
                        lands.append((i+dx, j+dy))
            return
                
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    grid[i][j] = '0'
                    submerge_island(i, j)
        return ans
        
# @lc code=end

