#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#

# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.ans = []
        self.res = 0
        self.target = target
        self.num = num
        self.n = len(num)
        self.backtrack([], 0, 0, 0)
        return self.ans

    def backtrack(self, expr, i, cur_val, cur_mul):
        if i == self.n:
            if cur_val == self.target:
                self.ans.append(''.join(expr))
            return
        sign_index = len(expr)
        if i > 0:
            expr.append('')
        val = 0
        for j in range(i, self.n):
            if (j>i and self.num[i]=='0'):
                break
            val = 10 * val + int(self.num[j])
            expr.append(self.num[j])
            if i==0:
                self.backtrack(expr, j+1, val, val)
            else:
                expr[sign_index] = '+'
                self.backtrack(expr, j+1, cur_val+val, val) 
                expr[sign_index] = '-'
                self.backtrack(expr, j+1, cur_val-val, -val) 
                expr[sign_index] = '*'
                self.backtrack(expr, j+1, cur_val-cur_mul + val*cur_mul, cur_mul*val)
        del expr[sign_index:]
# @lc code=end

