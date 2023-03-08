class Solution:
    def binary(self, L: list, start: int, column: bool, target: int) -> bool:
        left = start
        right = len(L) - 1 if column else len(L[0]) - 1
        if column:
            while left <= right:                #列
                mid = left + (right - left) // 2
                if target < L[mid][start]:
                    right = mid - 1
                elif target > L[mid][start]:
                    left = mid + 1
                else:
                    return True
        else:
            while left <= right:                #行
                mid = left + (right - left) // 2
                if target < L[start][mid]:
                    right = mid - 1
                elif target > L[start][mid]:
                    left = mid + 1
                else:
                    return True
        return False

    def searchMatrix(self, matrix: list, target: int) -> bool:
        if not matrix or not matrix[0]: return False
        if target < matrix[0][0] or target > matrix[len(matrix) - 1][len(matrix[0]) - 1]: return False
        for i in range(min(len(matrix[0]),len(matrix))):
            if target <= matrix[i][len(matrix[0]) - 1] or target <= matrix[len(matrix) - 1][i]:
                col = self.binary(matrix, i, True, target)
                row = self.binary(matrix, i, False, target)
                print(col,row)
                if row or col:
                    return True
        return False

    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

M = [[-1,3]]
case = Solution()
case.printMatrix(M)
print(case.searchMatrix(M,3))
