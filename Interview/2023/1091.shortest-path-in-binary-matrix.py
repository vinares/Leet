#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
from heapq import heappop, heappush
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        solution = [[n*n+1] * n for _ in range(n)]
        def score(x, y, cost):
            return max(n-x, n-y)+cost

        def available(x, y):
            return x >= 0 and x < n and y >= 0 and y < n and grid[x][y] == 0
        
        h = []
        if grid[0][0] == 0:
            heappush(h, (score(0, 0, 1), 1, (0, 0)))
            solution[0][0] = 1
        while h:
            f, g, point = heappop(h)
            x, y = point
            if x == n-1 and y == n-1: break
            for dx in range(-1, 2):
                nx = dx+x
                for dy in range(-1, 2):
                    ny = dy+y
                    if available(nx, ny) and solution[nx][ny] > g+1:
                        solution[nx][ny] = g+1
                        heappush(h, (score(nx, ny, g+1), g+1, (nx, ny)))
        return solution[-1][-1] if solution[-1][-1] < n*n+1 else -1
# @lc code=end

