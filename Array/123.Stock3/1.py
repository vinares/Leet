class Solution:
    def maxProfit(self, prices: int) -> int:
        n = len(prices)
        if n < 2: return 0
        dp = [[0, -prices[0]] for _ in range(3)]
        for i in range(1, n):
            dp[2][0] = max(dp[2][0], dp[1][1] + prices[i])
            dp[1][1] = max(dp[1][1], dp[1][0] - prices[i])
            dp[1][0] = max(dp[1][0], dp[0][1] + prices[i])
            dp[0][1] = max(dp[0][1], dp[0][0] - prices[i])
        return dp[2][0]
prices = [1,2,4,2,5,7,2,4,9,0]
print(Solution().maxProfit(prices))