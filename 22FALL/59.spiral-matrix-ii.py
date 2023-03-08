#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [[-1 for _ in range(n)] for _ in range(n)]

        i, j = 0, 0
        movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_mov = 0
        x, y = 0, 0
        for i in range(n*n):
            answer[x][y] = i+1
            nx, ny = x+movement[cur_mov][0], y+movement[cur_mov][1]
            if nx <0 or ny <0 or nx>=n or ny>=n or answer[nx][ny] != -1:
                cur_mov = (cur_mov+1)%4
                nx, ny = x+movement[cur_mov][0], y+movement[cur_mov][1]
            x, y = nx, ny
        return answer
# @lc code=end

