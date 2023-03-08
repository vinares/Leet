#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '[' or c.isalpha():
                stack.append(c)
            elif ord('0')<=ord(c)<=ord('9'):
                if stack and type(stack[-1]) == int:
                    prev_val = stack.pop()
                    stack.append(prev_val * 10 + int(c))
                else:
                    stack.append(int(c))
            else:
                string = []
                while(1):
                    cur = stack.pop()
                    if cur == '[':break
                    string.append(cur)
                multiplier = stack.pop()
                string = multiplier * ''.join(string[::-1])
                stack.append(string)
        return ''.join(stack) 
# @lc code=end

