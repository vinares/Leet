#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num)//2+1):
            a_str = num[:i]
            if i>1 and a_str[0] == '0':
                break
            a = int(a_str)
            for j in range(i+1, len(num)//3*2+1):
                b_str = num[i:j]
                if j > i+1 and b_str[0] == '0':
                    break
                b = int(b_str)
                res_str = a_str+b_str
                _a = a
                while len(res_str) < len(num):
                    s = _a + b
                    res_str += str(s)
                    _a = b
                    b = s
                if res_str == num:
                    return True
        return False



# @lc code=end

