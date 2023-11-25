#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tag = [[0] * n for _ in range(n)]
        moves = (1, 0, -1, 0, 1)
        area = {}

        def valid(x, y):
            return x >= 0 and x < n and y >= 0 and y < n and grid[x][y] == 1

        def mark(x, y, t, tag, area):
            if valid(x, y):
                if tag[x][y] == 0:
                    tag[x][y] = t
                    area[t] += 1
                    for i in range(4):
                        dx, dy = moves[i], moves[i+1]
                        mark(x+dx, y+dy, t, tag, area)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    t = i * n + j + 1
                    area[t] = 0
                    mark(i, j, t, tag, area)

        ans = max(area.values(), default=0)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    cur_area = 1
                    connected = set()
                    for k in range(4):
                        dx, dy = moves[k], moves[k+1]
                        x, y = dx + i, dy + j
                        if valid(x, y) and tag[x][y] not in connected:
                            connected.add(tag[x][y])
                            cur_area += area[tag[x][y]]
                    ans = max(ans, cur_area)
        return ans


# @lc code=end

