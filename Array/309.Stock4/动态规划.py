class Solution:
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if n < 2: return 0

        empty, freeze, hold = 0, 0, -prices[0]

        for i in range(1, n):
            freeze, empty, hold = hold + prices[i], max(empty, freeze), max(hold, empty - prices[i])
            print(prices[i], empty, freeze, hold)
        return max(empty, freeze)

prices = [1,2,3,0,2]
print(Solution().maxProfit(prices))