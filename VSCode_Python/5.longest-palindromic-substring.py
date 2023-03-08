#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        longest = 0
        res = [0, 1]
        parity = [0, 1]
        for i in range(len(s)):
            for par in parity:
                left, right = i, i + par
                while left >=0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                if right - left - 1 > longest:
                    longest = right - left - 1
                    res = [left+1, right]
        return s[res[0]:res[1]]
        
# @lc code=end

