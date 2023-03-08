#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pos = -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                found = True
                for j in range(len(needle)):
                    if i+j >= len(haystack) or haystack[i+j] != needle[j]:
                        found = False
                        break
                if found:
                    pos = i
                    break
        return pos
# @lc code=end

