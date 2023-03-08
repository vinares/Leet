class Solution:
    def maxProfit(self, k: int, prices: list) -> int:
        if not prices or k < 1: return 0
        n = len(prices)
        k = min(k, n//2)
        buy, sell = [-prices[0]] * (k+1), [0] * (k+1)

        for j in range(1, n):
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i-1] - prices[j])
                sell[i] = max(sell[i], buy[i] + prices[j])
                print(buy, sell)
        return sell[k]

k = 2
prices = [3,2,6,5,0,3]
print(Solution().maxProfit(k, prices))