#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isP(s):
            return s==s[::-1]
        n = len(s)
        if isP(s):
            return True
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return isP(s[:i]+s[i+1:]) or isP(s[:n-i-1] + s[n-i:])

# @lc code=end

