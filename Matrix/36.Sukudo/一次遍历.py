class Solution:
    def isValidSudoku(self, board: list) -> bool:
        row =  [[0] * 9 for i in range(9)]
        column = [[0] * 9 for i in range(9)]
        each = [[0] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                num = ord(board[i][j]) - ord('0')
                k = 3 * (i // 3) + j//3
                if 0 < num <= 9 :
                    row[i][num -1] += 1
                    column[j][num-1] += 1
                    each[k][num-1] += 1
                    if (row[i][num-1] > 1 or column[j][num-1] > 1 or each[k][num-1] > 1):
                        return False
        return True

    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

M = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
case = Solution()
case.printMatrix(M)
print(case.isValidSudoku(M))