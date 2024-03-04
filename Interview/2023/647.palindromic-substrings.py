#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        def make_p(i, j):
            ans = 0
            while i >=0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                ans += 1
            return ans
        
        return sum(make_p(i, i) + make_p(i,i+1) for i in range(len(s)))


# @lc code=end

