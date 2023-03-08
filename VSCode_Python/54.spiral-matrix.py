#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        ans = []
        while matrix:
            ans.extend(matrix[0])
            matrix = list(zip(*matrix[1::]))[::-1]
        return ans
        """
        m, n = len(matrix), len(matrix[0])
        ans = []
        i, j = 0, 0
        movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_mov = 0
        x, y = 0, 0
        while len(ans) < m * n:
            ans.append(matrix[x][y])
            matrix[x][y] = -1000
            nx, ny = x+movement[cur_mov][0], y+movement[cur_mov][1]
            if nx <0 or ny <0 or nx>=m or ny>=n or matrix[nx][ny] == -1000:
                cur_mov = (cur_mov+1)%4
                nx, ny = x+movement[cur_mov][0], y+movement[cur_mov][1]
            x, y = nx, ny
        return ans

# @lc code=end

