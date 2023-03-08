#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        left = len(num) - k
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)
        return ''.join(stack[:left]).lstrip('0') or '0'


# @lc code=end

