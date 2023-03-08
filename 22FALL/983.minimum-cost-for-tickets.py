#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [10 ** 9] * 366
        dp[-1] = 0
        
        for i in range(364, -1, -1):
            if i+1 in days:
                dp[i] = dp[i+1] + min(costs)
                if i+7<365:
                    dp[i] = min(dp[i], dp[i+7]+costs[1])
                if i+30<365:
                    dp[i] = min(dp[i], dp[i+30]+costs[2])
            else:
                dp[i] = dp[i+1]
        return dp[0]


# @lc code=end

