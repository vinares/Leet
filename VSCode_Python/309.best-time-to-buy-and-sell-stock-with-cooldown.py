#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        rest, buy, sell = 0, -prices[0], -1000
        for i in range(n):
            tr, tb, ts = rest,  buy, sell
            tr = max(rest, sell)
            tb = max(rest - prices[i], buy)
            ts = buy + prices[i]
            rest, buy, sell = tr, tb, ts
        return max(rest, sell)

# @lc code=end

