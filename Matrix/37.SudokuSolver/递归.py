class Solution:
    def solveSudoku(self, board: list) -> list:
        row = [[False] * 9 for i in range(9)]
        column = [[False] * 9 for i in range(9)]
        each = [[False] * 9 for i in range(9)]
        pos = 0
        blank = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    blank.append((i,j))
                else:
                    num = int(board[i][j])
                    row[i][num-1], column[j][num-1], each[i//3*3 + j//3][num-1] = True, True, True
        tot = len(blank)
        flag = 1
        def DFS(pos):
            nonlocal flag
            if pos == tot:
                flag = 0
                return
            i, j = blank[pos]
            for num in range(1,10):
                if not (row[i][num-1] or column[j][num-1] or each[i//3*3 + j//3][num-1]):
                    row[i][num - 1], column[j][num - 1], each[i // 3 * 3 + j // 3][num - 1] = True, True, True
                    board[i][j] = str(num)
                    DFS(pos+1)
                    row[i][num - 1], column[j][num - 1], each[i // 3 * 3 + j // 3][num - 1] = False, False, False
                if not flag:
                    return
        while flag:
            DFS(pos)
        return board

    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

M = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
case = Solution()
case.printMatrix(M)
N = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
case.printMatrix(case.solveSudoku(M))
case.printMatrix(N)
print(type(bin(1 << 3)))