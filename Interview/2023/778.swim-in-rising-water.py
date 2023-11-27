#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        scores = [[math.inf for i in range(n)] for _ in range(n)]
        h = [(grid[0][0], 0, 0)]
        moves = (1, 0, -1, 0, 1)
        heapq.heapify(h)
        while h:
            cur_score, x, y = heapq.heappop(h)
            if cur_score < scores[x][y]:
                scores[x][y] = cur_score
                for i in range(4):
                    dx, dy = moves[i], moves[i+1]   
                    X, Y = x+dx, y+dy
                    
                    if X >= 0 and X < n and Y>=0 and Y < n:
                        if X == n-1 and Y == n-1:
                            return max(cur_score, grid[X][Y])
                        heapq.heappush(h, (max(cur_score, grid[X][Y]), X, Y))
        return scores[n-1][n-1]



# @lc code=end

