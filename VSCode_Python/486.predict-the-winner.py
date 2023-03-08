#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#

# @lc code=start

from functools import lru_cache
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def backtrack(array, player1, player2, player1turn):
            if not array:
                if player1 >= player2:
                    return True
                else: 
                    return False
            if player1turn:
                return backtrack(array[1:], player1+array[0], player2, False) or backtrack(array[:-1], player1+array[-1], player2, False)
            else:
                return backtrack(array[1:], player1, player2+array[0], True) and backtrack(array[:-1], player1, player2+array[-1], True)


        return backtrack(tuple(nums), 0, 0, True)

# @lc code=end

