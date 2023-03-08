class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        def dfs(rest, i, ans):
            if rest == 0:
                return ans
            elif i < 0:
                return -1
            if rest < coins[i]:
                return dfs(rest, i - 1, ans)
            else:
                ans += 1
                rest -= coins[i]
                return dfs(rest, i, ans)


        return dfs(amount, len(coins) - 1, 0)


coins = [1,2,5]
amount = 103
print(Solution().coinChange(coins, amount))