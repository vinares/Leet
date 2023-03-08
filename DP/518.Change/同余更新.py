class Solution:
    def change(self, amount: int, coins: list) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i - coin]
        return dp[amount]

case = Solution()
amount = 5
coins = [1, 2, 5]
print(case.change(amount,coins))