class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        if not matrix or not matrix[0]: return False
        column, row = len(matrix[0]), len(matrix)
        if target < matrix[0][0] or target > matrix[row - 1][column - 1]: return False
        left, right = 0, row - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target < matrix[mid][0]:
                right = mid
            elif target > matrix[mid][0]:
                if target > matrix[mid][column -1]:
                    left = mid + 1
                    if target < matrix[left][0]:
                        return False
                else:
                    left = right + 1
            else:
                return True
        left, right =0, column - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target < matrix[mid][middle]:
                right = middle
            elif target > matrix[mid][middle]:
                left = middle + 1
                if target < matrix[mid][left]:
                    return False
            else:
                return True
        return False

    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

M = [[1,3],[2,4]]
case = Solution()
case.printMatrix(M)
print(case.searchMatrix(M,2))
