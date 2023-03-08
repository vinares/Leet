#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        min_cost = [float('inf')] * n
        ans = float('inf')
        min_cost[src] = 0
        for i in range(1, k+2):
            tmp = [x for x in min_cost]
            for start, end, price in flights:
                tmp[end] = min(tmp[end], min_cost[start]+price)
            min_cost = tmp
            ans = min(ans, min_cost[dst])
        return ans if ans < float('inf') else -1


# @lc code=end

