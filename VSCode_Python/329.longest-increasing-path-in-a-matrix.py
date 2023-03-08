#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dircs = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        mem = {}
        def dfs(i, j):
            if (i, j) in mem:
                return mem[(i, j)]
            best = 1
            for dx, dy in dircs:
                x, y = dx+i, dy+j
                if 0<=x<m and 0<=y<n and matrix[x][y] > matrix[i][j]:
                    best = max(best, dfs(x, y)+1)
            mem[(i, j)] = best
            return mem[(i, j)]

        a = 0
        for i in range(m):
            for j in range(n):
                dfs(i, j)
                a = max(a, mem[(i, j)])
        return a
# @lc code=end

