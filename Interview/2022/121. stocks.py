import copy
class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices) < 2: return 0
        diff = copy.copy(prices)
        for i in range(len(diff) - 2, -1, -1):
            diff[i] = max(diff[i], diff[i+1])
        diff[0] -= prices[0]
        for i in range(1, len(diff)):
            diff[i] = max(diff[i] - prices[i], diff[i - 1])
        return diff[-1]

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))