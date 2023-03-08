#
# @lc app=leetcode id=2281 lang=python3
#
# [2281] Sum of Total Strength of Wizards
#

# @lc code=start
from platform import java_ver


class Solution:
    def totalStrength(self, strength:list) -> int:
        n = len(strength)
        left, right = [-1] * n, [n] * n
        monotonic_stack = []
        prefix_sum = [0]
        sum_prefix_sum = [0,0]
        for i, s in enumerate(strength):
            while monotonic_stack and s <= strength[monotonic_stack[-1]]:
                x = monotonic_stack.pop()
                right[x] = i
            if monotonic_stack:
                left[i] = monotonic_stack[-1]
            monotonic_stack.append(i)
            prefix_sum.append(prefix_sum[-1]+s)
            sum_prefix_sum.append(sum_prefix_sum[-1]+prefix_sum[-1])
        
        ans, mod = 0, 10 ** 9 + 7
        for i, s in enumerate(strength):
            L, R = left[i]+1, right[i]-1
            s_sum = (i-L+1) * (sum_prefix_sum[R+2]-sum_prefix_sum[i+1]) - (R - i + 1) * (sum_prefix_sum[i+1] - sum_prefix_sum[L])
            ans = (ans + s * s_sum) % mod
        return ans
strength = [1,3,1,2]
print(Solution().totalStrength(strength))
# @lc code=end

