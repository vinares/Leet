class Solution:
    def trapRainWater(self, heightMap: list) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m < 2 or n < 2:
            return 0
        left, right = [[0 for _ in range(n)] for i in range(m)], [[0 for _ in range(n)] for i in range(m)]
        for i in range(m):
            left[i][0], right[i][n - 1] = heightMap[i][0], heightMap[i][n - 1]
        up, down = [[0 for _ in range(n)] for i in range(m)], [[0 for _ in range(n)] for i in range(m)]
        for i in range(n):
            up[0][i], down[m - 1][i] = heightMap[0][i], heightMap[m - 1][i]
        ans = 0

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                left[i][j] = min(max(left[i][j - 1], heightMap[i][j]), up[i][j - 1])
                up[i][j] = min(max(up[i - 1][j], heightMap[i][j]), left[i - 1][j])
        for i in range(m - 2, 0, -1):
            for j in range(n - 2, 0, -1):
                right[i][j] = max(right[i][j + 1], heightMap[i][j], down[i][j + 1])
                down[i][j] = max(down[i + 1][j], heightMap[i][j], right[i + 1][j])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                wood = min(left[i][j], right[i][j], up[i][j], down[i][j])
                if heightMap[i][j] < wood:
                    print(i,j,wood,heightMap[i][j])
                    ans += wood - heightMap[i][j]
        return ans

print(Solution().trapRainWater(heightMap=[[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))