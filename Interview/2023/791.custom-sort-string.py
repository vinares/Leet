#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mem = defaultdict(int)
        rest = ''
        for char in s:
            if char in order:
                mem[char] += 1
            else:
                rest += char
        for char in order:
            rest += mem.get(char, 0) * char
        return rest

# @lc code=end

