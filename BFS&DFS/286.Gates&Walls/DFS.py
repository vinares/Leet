class Solution:
    def WallsAndGates(self, rooms):
        m, n =len(rooms), len(rooms[0])
        ans = [[0 for _ in range(n)] for j in range(m)]
        INF = 2147483647
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False for _ in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 'INF':
                    ans[i][j] = INF
                else:
                    ans[i][j] = int(rooms[i][j])

        def dfs(x, y):
            nonlocal ans, visited
            visited[x][y] =True
            for dire in directions:
                X, Y = x + dire[0], y + dire[1]
                if -1 < X < m and -1 < Y < n:
                    if ans[X][Y] == -1:continue
                    else:
                        ans[X][Y] = min(ans[X][Y], ans[x][y] + 1)
                        if not visited[X][Y] and ans[X][Y] > -1:
                            dfs(X, Y)
            return

        for i in range(m):
            for j in range(n):
                if ans[i][j] == 0 and not visited[i][j]:
                    dfs(i, j)

        return ans


rooms = [['INF', '-1', '0', 'INF'], ['INF', 'INF', 'INF', '-1'], ['INF', '-1', 'INF', '-1'], ['0', '-1', 'INF', 'INF']]
print(Solution().WallsAndGates(rooms))