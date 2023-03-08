class Solution:
    def isValidSudoku(self, board: list) -> bool:

        for i in range(9):
            numset = set()
            for j in range(9):
                x = board[i][j]
                if '0' < x <= '9':
                    if x in numset:
                        return False
                    else:
                        numset.add(x)

        for i in range(9):
            numset = set()
            for j in range(9):
                x = board[j][i]
                if '0' < x <= '9':
                    if x in numset:
                        return False
                    else:
                        numset.add(x)

        for i in range(3):
            for j in range(3):
                numset = set()
                for k in range(3):
                    for l in range(3):
                        x = board[3*i+k][3*j+l]
                        if '0' < x <= '9':
                            if x in numset:
                                return False
                            else:
                                numset.add(x)
        return True

    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

M = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".","9",".",".",".",".",".",".","1"],["8",".",".",".",".",".",".",".","."],[".","9","9","3","5","7",".",".","."],[".",".",".",".",".",".",".","4","."],[".",".",".","8",".",".",".",".","."],[".","1",".",".",".",".","4",".","9"],[".",".",".","5",".","4",".",".","."]]

case = Solution()
case.printMatrix(M)
print(case.isValidSudoku(M))