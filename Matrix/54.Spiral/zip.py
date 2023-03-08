
class Solution:
    def spiralOrder(self, matrix: list) -> list:
        if not matrix or not matrix[0]: return matrix
        data = []
        while matrix:
            data += matrix.pop(0)
            matrix = list(zip (*matrix))[::-1]
        return data

    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

M = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
case = Solution()
print(case.spiralOrder(M))