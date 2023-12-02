#
# @lc app=leetcode id=2060 lang=python3
#
# [2060] Check if an Original String Exists Given Two Encoded Strings
#

# @lc code=start
from functools import lru_cache
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        def parse_int(s, p):
            start = p
            while p < len(s) and s[p].isdigit():
                p += 1
                yield int(s[start:p]), p
                
        @lru_cache(None)
        def bt(i, j, d):
            if i == m and j == n:
                return d == 0
            elif i < m and s1[i].isdigit():
                return any([bt(p, j, d+val) for val, p in parse_int(s1, i)])
            elif j < n and s2[j].isdigit():
                return any([bt(i, p, d-val) for val, p in parse_int(s2, j)])
            elif d == 0 and i < m and j < n:
                return s1[i] == s2[j] and bt(i+1, j+1, d) 
            elif d > 0 and j < n:
                return bt(i, j+1, d-1)
            elif d < 0 and i < m:
                return bt(i+1, j, d+1)
            return False
        return bt(0, 0, 0)

# @lc code=end

