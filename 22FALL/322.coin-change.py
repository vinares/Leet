#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count_to_achieve_amounts = [amount+1 for _ in range(amount+1)]
        count_to_achieve_amounts[0] = 0
        for amt in range(1, amount+1):
            if amt in coins:
                count_to_achieve_amounts[amt] = 1 
            else:
                for coin in coins:
                    if amt - coin >= 0:
                        count_to_achieve_amounts[amt] = min(count_to_achieve_amounts[amt-coin]+1, count_to_achieve_amounts[amt])
        return count_to_achieve_amounts[amount] if (count_to_achieve_amounts[amount] < amount + 1) else -1

# @lc code=end

