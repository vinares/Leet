#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0: return 1
        cur, ans = 9, 10
        for i in range(1, min(11, n)):
            cur = cur * (10-i)
            ans += cur
        return ans
# @lc code=end

