#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        i, j =0, len(s) -1
        while i <= j and not s[i].isalnum():
            i += 1
        while i <= j and not s[j].isalnum():
            j -= 1
        if i > j: return True
        return s[i].lower() == s[j].lower() and self.isPalindrome(s[i+1:j])

# @lc code=end

