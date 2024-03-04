#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        moves = []
        x, y = click
        if board[x][y] == 'M': 
            board[x][y] = 'X'
            return board
        for i in (0, 1, -1):
            for j in (0, 1, -1):
                if (i ==0 and j == 0): continue
                moves.append((i ,j))
        def inside(i, j):
            return i >= 0 and i < m and j >= 0 and j < n
        
        q = [tuple(click)]
        def count_bomb(x, y):
            cnt = 0
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if inside(nx, ny):
                    if board[nx][ny] in 'MX':
                        cnt +=1 
            return cnt

        if count_bomb(x, y) > 0:
            board[x][y] = str(count_bomb(x, y))
            return board

        while q:
            new_q = set()
            for x, y in q:
                board[x][y] = 'B'
                for dx, dy in moves:
                    nx, ny = dx+x, dy+y
                    if inside(nx, ny) and board[nx][ny] == 'E':
                        cnt = count_bomb(nx, ny)
                        if cnt == 0:
                            new_q.add((nx, ny))
                        else:
                            board[nx][ny] = str(cnt)
            q = list(new_q)
        return board

        

# @lc code=end

