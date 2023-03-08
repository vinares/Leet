#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        decimal = 1
        start, end = 1, 9
        count = 9
        while n > count*decimal:
            n -= count*decimal
            start *= 10
            end = end * 10 + 9
            count = (end-start) + 1
            decimal += 1
        number_index = (n-1) // decimal
        number_digit = (n-1) % decimal
        return int(str(start+number_index)[number_digit])

# @lc code=end

