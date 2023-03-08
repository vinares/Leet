#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}
        def dp(i, j):
            if j >= len(p): return i == len(s)
            elif i >= len(s): 
                return dp(i, j+2) and j+1 < len(p) and p[j+1] == '*'
            if (i, j) not in mem:
                matched = p[j] == '.' or s[i] == p[j]
                if j+1 < len(p) and p[j+1] == '*':
                    mem[(i, j)] = dp(i, j+2) or ( matched and dp(i+1, j))
                else:
                    mem[(i, j)] = matched and dp(i+1, j+1)
            return mem[(i, j)]
        return dp(0, 0)
# @lc code=end

