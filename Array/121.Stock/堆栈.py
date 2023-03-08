class Solution:
    def maxProfit(self, prices: list) -> int:
        n = len(prices)
        if n < 2: return 0
        ans = 0
        buy = [0]
        sell = [n - 1]
        for i in range(1, n - 1):
            if prices[i] < prices[buy[-1]]:
                if i - 1 == buy[-1] and len(buy) > 1:
                    buy.pop()
                buy.append(i)
        for i in range(n - 2, 0, -1):
            if prices[i] > prices[sell[-1]]:
                if i + 1 == sell[-1] and len(buy) > 1:
                    sell.pop()
                sell.append(i)

        for i in range(len(buy)):
            for j in range(len(sell)):
                if buy[i] < sell[j] and prices[sell[j]] > prices[buy[i]]:
                    ans = max(ans, prices[sell[j]] - prices[buy[i]])
        return ans
prices = [3,3,5,0,0,3,1,4]
print(Solution().maxProfit(prices))