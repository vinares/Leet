#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s):
        num, res, stack, sign = 0, 0, [], 1
        for c in s:
            if c.isdigit():
                num *= 10
                num += int(c)
            elif c in '-+':
                res += sign * num
                num = 0
                sign = [1, -1][c=='-']
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ')':
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign


# @lc code=end

