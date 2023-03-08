class Solution:
    def solve(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visisted = [[False for i in range(n)] for j in range(m)]
        directions =  [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs1(x, y):
            visisted[x][y] = True
            for dire in directions:
                X, Y = x + dire[0], y + dire[1]
                if -1 < X < m and -1 < Y < n and not visisted[X][Y] and board[X][Y] == 'O':
                    dfs1(X, Y)

        def dfs2(x, y):
            nonlocal visisted, board
            visisted[x][y] = True
            board[x][y] = 'X'
            for dire in directions:
                X, Y = x + dire[0], y + dire[1]
                if 0 < X < m - 1 and 0 < Y < n - 1 and not visisted[X][Y] and board[X][Y] == 'O':
                    dfs2(X, Y)


        for i in range(m):
            if not visisted[i][0] and board[i][0] == 'O':
                dfs1(i,0)
            if not visisted[i][n - 1] and board[i][n - 1] == 'O':
                dfs1(i, n - 1)
        for i in range(n):
            if not visisted[0][i] and board[0][i] == 'O':
                dfs1(0, i)
            if not visisted[m - 1][i] and board[m - 1][i] == 'O':
                dfs1(m - 1, i)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not visisted[i][j] and board[i][j] == 'O':
                    dfs2(i,j)

        return board


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)
print(board)