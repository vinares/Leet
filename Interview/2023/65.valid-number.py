#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
from collections import Counter
class Solution:
    def isNumber(self, s: str) -> bool:
        screening = Counter(s)
        if screening['e']+ screening['E']> 1 or screening['.'] > 1 or screening['+'] > 1 or screening['-'] > 1:
            return False
        decimal = s
        sci = s.split('e')
        if len(sci) == 2:
            if sci[1] == '': return False
            decimal = sci[0]
        sci = s.split('E')
        if len(sci) == 2:
            if sci[1] == '': return False
            decimal = sci[0]
        if not decimal: return False
        if decimal[0] in '-+':
            decimal = decimal[1:]
        decimals = decimal.split('.')
        if len(decimals) == 2:
            if decimals[0] and not decimals[0].isdigit(): return False
            if decimals[1] and not decimals[1].isdigit(): return False
            if not decimals[0] and not decimals[1]: return False
        elif len(decimals) == 1:
            if not decimals[0] or not decimals[0].isdigit(): return False
        return True

# @lc code=end

