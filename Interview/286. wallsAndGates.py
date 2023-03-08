import copy
class Solution:
    def wallsAndGates(self, rooms: list):
        if not rooms: return []
        m, n = len(rooms), len(rooms[0])
        ans = copy.copy(rooms)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j, d, rooms):
            if rooms[i][j] == -1: return

            for xd,yd in directions:
                x, y = i + xd, j + yd
                if 0 <= x <m and 0 <= y <n and rooms[x][y] > rooms[i][j]:
                    rooms[x][y] = d + 1
                    dfs(x, y, d + 1, rooms)
            return

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dfs(i, j, 0, rooms)
        return rooms

INF = 2^31 - 1
rooms = [[INF , -1 , 0 , INF],
         [INF ,INF, INF , -1],
         [INF  ,-1 ,INF , -1],
         [  0  ,-1 ,INF ,INF]]
print(Solution().wallsAndGates(rooms))