class Solution:
    def maxProfit(self, prices: int) -> int:
        n = len(prices)
        if n < 2: return 0

        dp0, dp1 = 0, -prices[0]
        for i in range(1, n):
            dp0_t = max(dp0, dp1 + prices[i])
            dp1_t = max(dp1, dp0 - prices[i])
            dp1 = dp1_t
            dp0 = dp0_t
        return dp0


prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))