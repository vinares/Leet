#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#

# @lc code=start

class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n!=1:
            if n % 2 == 0:
                ans += 1
                n //= 2
            elif n % 4 == 1:
                ans += 2
                n //= 2
            else:
                if n == 3:
                    ans += 2
                    n = 1
                else:
                    ans += 2
                    n = n // 2 + 1
        return ans
# @lc code=end

