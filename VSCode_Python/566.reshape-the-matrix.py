#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not mat:
            return mat
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        ans = [[0 for _ in range(c)] for i in range(r)]
        x, y = 0, 0
        for i in range(m):
            for j in range(n):
                num = mat[i][j]
                if x == c:
                    y += 1
                    x = 0
                ans[y][x] = num
                x += 1
        return ans
# @lc code=end

