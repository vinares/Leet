#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for bracket in s:
            if bracket in mapping:
                stack.append(bracket)
            else:
                if not stack or bracket!=mapping[stack[-1]]:
                    return False
                stack.pop()
        return not stack
# @lc code=end