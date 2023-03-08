#
# @lc app=leetcode id=521 lang=python3
#
# [521] Longest Uncommon Subsequence I
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b: return -1  
        alen, blen = len(a), len(b)
        return alen if alen > blen else blen




# @lc code=end

