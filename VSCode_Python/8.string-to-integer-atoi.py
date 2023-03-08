#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        s = s[i::]
        if not s:
            return 0
        aggre = 0
        i = 0
        alge = ['-', '+']
        nums = [str(i) for i in range(10)]
        flag = 1
        if s[i] == '-':
            flag = -1
        if s[i] in alge:
            i += 1
        while i < len(s) and s[i] in nums:
            aggre *= 10
            aggre += int(s[i])
            i += 1
        aggre *= flag
        if aggre < - 2 ** 31:
            aggre = - 2 ** 31
        if aggre > 2 ** 31 - 1:
            aggre = 2 ** 31 - 1
        return aggre

# @lc code=end

