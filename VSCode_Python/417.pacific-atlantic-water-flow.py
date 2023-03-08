#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    moves = [0, 1, 0, -1, 0]
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def search(ocean):
            visited = set()
            def dfs(i, j):
                if (i, j) in visited:
                    return
                visited.add((i, j))
                for k in range(4):
                    x, y = i+self.moves[k],j + self.moves[k+1]
                    if x < m and x >= 0 and y < n and y >= 0 and heights[x][y] >= heights[i][j]:
                        dfs(x, y)
            for i, j in ocean:
                dfs(i, j)
            return visited
        pacific = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        atlantic = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]
        return list(map(list, search(pacific) & search(atlantic)))
        

# @lc code=end

