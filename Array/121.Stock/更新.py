class Solution:
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if n < 2: return 0
        profit = 0
        lowest = prices[0]
        for price in prices:
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)
        return profit

prices = [3,3,5,0,0,3,1,4]
print(Solution().maxProfit(prices))