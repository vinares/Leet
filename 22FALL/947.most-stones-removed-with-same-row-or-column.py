#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start

from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        xs, ys = defaultdict(list), defaultdict(list)
        for x, y in stones:
            xs[x].append((x, y))
            ys[y].append((x, y))
        visited = set()

        def dfs(stone):
            if stone in visited:
                return
            visited.add(stone)

            for s in xs[stone[0]]:
                dfs(s)

            for s in ys[stone[1]]:
                dfs(s)
            return
        
        ans = 0
        for stone in stones:
            s = tuple(stone)
            if s not in visited:
                ans += 1
                dfs(s)
        return len(stones) - ans
# @lc code=end

