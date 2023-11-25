#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        elif n < 0: return 1/self.myPow(x, -n)
        ans = self.myPow(x*x, n//2)
        return ans * x if n&1 else ans

# @lc code=end

