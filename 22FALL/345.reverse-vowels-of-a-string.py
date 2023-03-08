#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        characters = [c for c in s]
        i, j = -1, len(s)
        vowels = 'aeiouAEIOU'
        while i < j:
            while i+1 < len(s):
                i += 1
                if s[i] in vowels:
                    break
            while j-1 >= 0:
                j -= 1
                if s[j] in vowels:
                    break
            if i < j:
                characters[i], characters[j] = characters[j], characters[i]
        return ''.join(characters)

# @lc code=end

