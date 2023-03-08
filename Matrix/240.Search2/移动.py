class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if not matrix or not matrix[0]: return False
        if target < matrix[0][0] or target > matrix[len(matrix) - 1][len(matrix[0]) - 1]: return False
        col, row = 0, len(matrix) - 1
        while 0 <= col < len(matrix[0]) and 0 <= row < len(matrix):
            if target > matrix[row][col]:
                col += 1
            elif target < matrix[row][col]:
                row -= 1
            else:
                return True
        return False

    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

M = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
case = Solution()
case.printMatrix(M)
print(case.searchMatrix(M,5))
