##corner: obstacles in above the object, or in between objects, but the object still can hit the ground.

class Solution:
    def tetrix(self,matrix):
        m, n = len(matrix), len(matrix[0])
        ans = [(0,0)] * n
        lowest_row =  None
        highest_obstacles = [None] * n
        lowest_objects = [None] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "*":
                    if lowest_row == None:
                        lowest_row = i
                    else:
                        lowest_row = max(lowest_row, i)
                    if lowest_objects[j] == None:
                        lowest_objects[j] = i
                    else:
                        lowest_objects[j] = max(lowest_objects[j], i)

                if matrix[i][j] == "#":
                    if highest_obstacles[j] == None:
                        highest_obstacles[j] = i
                    else:
                        highest_obstacles[j] = min(highest_obstacles[j], i)
        if lowest_row == None:return 0
        for j in range(n):
            if lowest_objects[j] == None or highest_obstacles[j] == None or highest_obstacles[j] > m  - 1 - (lowest_row - lowest_objects[j]):
                continue
            for i in range(0, m - lowest_row + 1):
                if matrix[i][j] == "#":
                    ans += 1
        return ans



mat = [ ["*", ".", "*", "*",".","."],
        ["*", "*", "*", ".",".","#"],
        [".", "*", ".", ".",".","."],
        ["#", ".", ".", ".",".","."],
        ["#", ".", ".", "#",".","."] ]

print(Solution().tetrix(mat))