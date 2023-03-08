#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#

# @lc code=start
from heapq import heapify, heappop, heappush
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])        
        visited = [[False for _ in range(n)] for i in range(m)]
        height_heap = []
        heapify(height_heap)
        for i in range(m):
            heappush(height_heap, (heightMap[i][0], i, 0))
            heappush(height_heap, (heightMap[i][n-1], i, n-1))
        for j in range(1, n-1):
            heappush(height_heap, (heightMap[0][j], 0, j))
            heappush(height_heap, (heightMap[m-1][j], m-1, j))
        dirs = [0, 1, 0, -1, 0]
        ans = 0
        while height_heap:
            water, i, j = heappop(height_heap)
            visited[i][j] = True
            for k in range(4):
                nx, ny = i+dirs[k], j+dirs[k+1]
                if nx >=0 and nx < m and ny >=0 and ny < n and visited[nx][ny] == False:
                    ans += max(0, water - heightMap[nx][ny])
                    visited[nx][ny] = 1
                    heappush(height_heap, (max(heightMap[nx][ny], water), nx, ny))
        return ans
              



# @lc code=end

