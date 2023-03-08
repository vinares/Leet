class Solution:
    def maxProfit(self, k: int, prices: list) -> int:
        n = len(prices)
        if n < 2: return 0

        dp = [[0, -prices[0]] for _ in range(k + 1)]

        for i in range(1, n):
            for j in range(k, 0, -1):
                dp[j][1] = max(dp[j][1], dp[j][0] - prices[i])
                dp[j][0] = max(dp[j][0], dp[j - 1][1] + prices[i])
            dp[0][1] = max(dp[0][1], dp[0][0] - prices[i])
        return dp[k][0]
prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
print(Solution().maxProfit(2, prices))