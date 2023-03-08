#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from copy import copy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a, b = copy(nums), copy(nums)
        ans = [1] * n
        for i in range(n - 1):
            a[i+1] *= a[i]
            b[n-2-i] *= b[n-1-i]
        for i in range(n):
            if i == 0:
                ans[i] = b[1]
            elif i == n - 1:
                ans[i] = a[n-2]
            else:
                ans[i] = a[i-1] * b[i+1]
        return ans
# @lc code=end

