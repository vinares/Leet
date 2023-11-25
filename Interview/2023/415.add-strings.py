#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ''
        i, j = len(num1)-1, len(num2)-1
        summ = 0
        flag = 0
        while i >= 0 and j >=0:
            summ = int(num1[i]) + int(num2[j]) + flag
            flag = 0
            if summ > 9:
                flag = 1
                summ -= 10
            ans += str(summ)
            i -= 1
            j -= 1
        while i >=0:
            summ = int(num1[i]) + flag
            flag = 0
            if summ > 9:
                flag = 1
                summ -= 10

            ans += str(summ)
            i -= 1
        while j >=0:
            summ = int(num2[j]) + flag
            flag = 0
            if summ > 9:
                flag = 1
                summ -= 10

            ans += str(summ)
            j -= 1
        if flag == 1:
            ans += '1'
        return ans[::-1]
# @lc code=end

