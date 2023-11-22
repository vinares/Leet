#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        num, sign, stack = 0, '+', []
        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if (not s[i].isdigit() and s[i]!= ' ') or i == n-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    prev = stack.pop()
                    stack.append(prev * num)
                elif sign == '/':
                    prev = stack.pop()
                    if ( prev // num < 0 and prev%num != 0):
                        stack.append( prev // num+1)
                    else:
                        stack.append( prev // num)
                num = 0
                sign = s[i]
        return sum(stack)

# @lc code=end

