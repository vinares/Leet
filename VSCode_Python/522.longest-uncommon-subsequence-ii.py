#
# @lc app=leetcode id=522 lang=python3
#
# [522] Longest Uncommon Subsequence II
#

# @lc code=start
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        if len(set(strs)) < len(strs): return -1
        ans = 0
        for str in strs:
            ans = max(ans, len(str))
        return ans
# @lc code=end

