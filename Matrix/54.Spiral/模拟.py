class Solution:
    def spiralOrder(self, matrix: list) -> list:
        if not matrix or not matrix[0]: return matrix
        column = len(matrix[0])
        row = len(matrix)
        data = []

        visited = [[False]* column for _ in range(row)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        c, r = 0, 0
        director = 0
        for i in range(column * row):
            data.append(matrix[r][c])
            visited[r][c] = True
            nextc, nextr = c + direction[director][1], r + direction[director][0]
            if not(0 <= nextc < column and 0 <= nextr < row and not visited[nextr][nextc]):
                director = (director + 1) % 4
            c += direction[director][1]
            r += direction[director][0]
        return data

    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

M = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
case = Solution()
case.printMatrix(M)
print(case.spiralOrder(M))

