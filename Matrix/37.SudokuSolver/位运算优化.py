class Solution:
    def solveSudoku(self, board: list) -> list:
        row = [0] * 9
        column = [0] * 9
        each = [0] * 9
        pos = 0
        blank = []

        def flip(i: int, j: int, digit: int):
            row[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            each[i // 3 * 3 + j // 3] ^= (1 << digit)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    blank.append((i,j))
                else:
                    num = int(board[i][j])
                    flip(i, j, num - 1)
        tot = len(blank)
        flag = 1

        def DFS(pos):
            nonlocal flag
            if pos == tot:
                flag = 0
                return

            i, j = blank[pos]
            mask = ~(row[i] | column[j] | each[i//3*3+j//3]) & 0x1ff
            import math
            while mask:
                digitmask = mask & (-mask)
                digit = int(math.log2(digitmask))
                flip(i,j,digit)
                board[i][j] = str(digit + 1)
                DFS(pos+1)
                flip(i,j,digit)
                mask &= (mask - 1)
                if not flag:
                    return
            return

        DFS(0)
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