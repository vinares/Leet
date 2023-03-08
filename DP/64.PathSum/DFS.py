class Solution:
    def minPathSum(self, grid: list) -> int:
        if not grid[0]:return 0
        m, n = len(grid), len(grid[0])
        dic = dict()
        def DFS(x: int, y: int) -> int:
            if x == m or y == n:
                return float('inf')
            if (x,y) in dic:
                return dic[(x,y)]
            p = min(DFS(x + 1, y), DFS(x, y + 1))
            dic[(x,y)] = grid[x][y] + (0 if p == float('inf') else p)

            print(dic)
            return dic[(x,y)]

        return DFS(0,0)

print(Solution().minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))