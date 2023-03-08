#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        characters = [c for c in s]
        n = len(s)
        i, j = 0, k-1
        while j < n:
            start = i
            while i < j:
                characters[i], characters[j] = characters[j], characters[i]
                i += 1
                j -= 1
            i = start + 2 * k
            j = i + k-1
        if i < n:
            j = n-1
            while i < j:
                characters[i], characters[j] = characters[j], characters[i]
                i += 1
                j -= 1
        return ''.join(characters)


# @lc code=end

