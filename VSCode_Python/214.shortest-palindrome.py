#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def isP(self, s):
        n = len(s)
        if n < 2:
            return True
        if n % 2 == 1:
            return s[0:n//2] == s[n//2+1:n][::-1]
        else:
            return s[0:n//2] == s[n//2:n][::-1]

    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n, -1, -1):
            if self.isP(s[0:i]):
                return s[i:n][::-1] + s

# @lc code=end

