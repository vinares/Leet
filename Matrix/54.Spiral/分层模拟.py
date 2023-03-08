
class Solution:
    def spiralOrder(self, matrix: list) -> list:
        if not matrix or not matrix[0]: return matrix
        column = len(matrix[0])
        row = len(matrix)
        data = []
        top, bottom, left, right = 0, row - 1, 0, column - 1
        while (top <= bottom and left <= right):
            for i in range(left, right + 1):
                data.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                data.append(matrix[i][right])
            if (top < bottom and left < right):
                for i in range(right - 1, left, -1):
                    data.append(matrix[bottom][i])
                for i in range(bottom, top, -1):
                    data.append(matrix[i][left])
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return data

    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

M = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
case = Solution()
case.printMatrix(M)
print(case.spiralOrder(M))