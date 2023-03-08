class Solution:
    def generateMatrix(self, n: int) -> list:
        matrix = [[0]*n for _ in range(n)]
        visited = [[False]*n for _ in range(n)]
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        index = 0
        counter = n * n
        column, row = 0, 0
        for i in range(1, n*n + 1):
            matrix[row][column] = i
            visited[row][column] = True
            nextr, nextc = row + direction[index][0], column + direction[index][1]
            if not (0 <= nextr < n and 0 <= nextc < n and not visited[nextr][nextc]):
                index = (index + 1) % 4
            row += direction[index][0]
            column += direction[index][1]
        return matrix
    def printMatrix(self, matrix: list):
        for i in range(len(matrix)):
            print(matrix[i])
        print('\n')

case = Solution()
case.printMatrix(case.generateMatrix(3))