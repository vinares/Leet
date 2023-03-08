#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n =  len(board), len(board[0])
        directions = [0, 1, 0, -1, 0]

        def dfs(i, j):
            if i < 0 or i > m-1 or j < 0 or j > n-1 or board[i][j] != 'O':
                return
            board[i][j] = 'Y'
            for k in range(4):
                dx, dy = directions[k], directions[k+1]
                x, y = i + dx, j + dy
                dfs(x, y)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n-1):
            dfs(0, j)
            dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Y':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return 

# @lc code=end

