#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s: return False
        ss = (s + s)[1:-1]
        return ss.find(s) != -1
# @lc code=end
