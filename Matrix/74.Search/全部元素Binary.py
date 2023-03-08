class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if not matrix or not matrix[0]: return False
        column, row = len(matrix[0]), len(matrix)
        if target < matrix[0][0] or target > matrix[row - 1][column - 1]: return False
        left, right = 0, column * row - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == matrix[mid // column][mid % column]:
                return True
            elif target < matrix[mid // column][mid % column]:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

M = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
case = Solution()
case.printMatrix(M)
print(case.searchMatrix(M,1))

