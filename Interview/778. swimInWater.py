import collections
import heapq

class Solution:
    def swimInWater(self, grid: list) -> int:
        n = len(grid)
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        q = [(grid[0][0],0,0)]
        grade = grid[0][0]
        heapq.heapify(q)

        while q:
            cur = heapq.heappop(q)
            grid[cur[1]][cur[2]] = -1
            grade = max(cur[0], grade)
            if cur[1] == n - 1 and cur[2] == n - 1:
                return grade
            for x, y in directions:
                X, Y = x + cur[1], y + cur[2]
                if 0 <= X < n and 0 <= Y < n and grid[X][Y] != -1:
                    heapq.heappush(q, (grid[X][Y],X, Y))

        return grade


grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(Solution().swimInWater(grid))