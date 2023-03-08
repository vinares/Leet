class Solution:
    def generateMatrix(self, n: int) -> list:
        matrix = [[0]*n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n-1
        total, num = n * n, 1
        while num <= total:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix
    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

case = Solution()
case.printMatrix(case.generateMatrix(3))