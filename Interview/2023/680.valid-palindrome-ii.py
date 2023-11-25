#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                p1 = s[left+1:right+1]
                p2 = s[left:right]
                return p1 == p1[::-1] or p2 == p2[::-1]
            left += 1
            right -= 1
        return True
        
# @lc code=end

