from heapq import *
class Solution:
    def trapRainWater(self, heightMap: list) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m < 2 or n < 2:
            return 0
        ans, imax = 0, 0
        visited = set()
        heap = []
        coor = [[0, 1], [-1, 0], [0, -1], [1, 0]]

        for i in range(n):
            visited.add((0,i))
            visited.add((m-1, i))
            heappush(heap, [heightMap[0][i], 0, i])
            heappush(heap, [heightMap[m - 1][i], m - 1, i])
        for i in range(m):
            visited.add((i, 0))
            visited.add((i,n-1))
            heappush(heap, [heightMap[i][0], i, 0])
            heappush(heap, [heightMap[i][n - 1], i, n - 1])

        while heap:
            cur = heappop(heap)
            imax = max(imax, cur[0])
            for x, y in coor:
                tmpx, tmpy = cur[1] + x, cur[2] + y
                if tmpx < 0 or tmpx > m - 1 or tmpy < 0 or tmpy > n - 1 or (tmpx,tmpy) in visited:
                    continue
                visited.add((tmpx, tmpy))
                if heightMap[tmpx][tmpy] < imax:
                    ans += imax - heightMap[tmpx][tmpy]
                heappush(heap, [heightMap[tmpx][tmpy], tmpx, tmpy])
        return ans

    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

print(Solution().trapRainWater(heightMap=[[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))