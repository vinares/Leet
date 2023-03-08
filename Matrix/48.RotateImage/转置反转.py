class Solution:
    def rotate(self, matrix: list) -> None:
        for i in range(len(matrix[0])):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

M = [[1,2,3],[4,5,6],[7,8,9]]
case = Solution()
case.printMatrix(M)
case.rotate(M)
case.printMatrix(M)

