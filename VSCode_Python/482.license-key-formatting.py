#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        new_s = []
        pointer = len(s)-1
        cur_s = []
        for i in range(len(s)-1, -1, -1):
            if s[i] == '-':
                continue
            cur_c = s[i].upper()
            cur_s.append(cur_c)

            if len(cur_s ) == k:
                new_s.append(''.join(cur_s))
                cur_s = []

        if cur_s:
            new_s.append(''.join(cur_s))
        return '-'.join(new_s)[::-1]
# @lc code=end

