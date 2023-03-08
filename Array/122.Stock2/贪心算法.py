class Solution:
    def maxProfit(self, prices: int) -> int:
        n = len(prices)
        if n < 2: return 0
        ans = 0

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))