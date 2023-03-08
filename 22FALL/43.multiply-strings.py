#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = [0 for _ in range(len(num1)+len(num2)-1)]
        
        for i, c in enumerate(num1):
            for j, d in enumerate(num2):
                ans[i+j] += int(c) * int(d)
        res = 0
        for i, x in enumerate(ans[::-1]):
            res += 10 ** i * x
        return str(res)



# @lc code=end

