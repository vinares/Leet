#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0: return False
        powers = [3 ** i for i in range(1, 5)]
        index = 3
        while index >= 0 and n > 1:
            if n % powers[index] == 0:
                n //= powers[index]
            else:
                index -= 1
        if n == 1:
            return True
        return False

# @lc code=end


