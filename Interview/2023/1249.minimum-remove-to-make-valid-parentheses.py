#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
from collections import Counter
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        right = Counter(s).get(')', 0)
        ans = []
        left = 0
        for char in s:
            if char not in '()':
                ans.append(char)
            elif char == '(' and left < right:
                ans.append(char)
                left += 1
            elif char == ')' and left > 0:
                left -= 1
                right -= 1
                ans.append(char)
            elif char == ')':
                right -= 1
        return ''.join(ans)
        

# @lc code=end

