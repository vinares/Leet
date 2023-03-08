#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        m, n = len(board), len(board[0])

        def cnt_neighbors(i, j):
            dxs = [-1, 1, 0]
            dys = [-1, 1, 0]
            cnt = 0
            for dx in dxs:
                for dy in dys:
                    x, y = i+dx, j+dy
                    if (x == i and y == j) or x < 0 or y < 0 or x >= m or y >= n:
                        continue
                    if board[x][y] in [1, 2]:
                        cnt += 1
            return cnt

        for i in range(m):
            for j in range(n):
                cnt = cnt_neighbors(i, j)
                if board[i][j] == 0 and cnt == 3:
                    board[i][j] = -1
                elif board[i][j] == 1 and cnt not in [2, 3]:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] ==  2:
                    board[i][j] = 0
        return

# @lc code=end

