#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int):
        ans = []

        def backtrack(tmp, l, r, lrest,rrest):
            if rrest == 0 and lrest == 0 and l == n and r == n:
                ans.append(tmp)
                return
            elif rrest == 0: 
                return
            if lrest > 0:
                backtrack(tmp + '(', l+1,r, lrest - 1, rrest)
            if l > r:
                backtrack(tmp + ')', l, r+1, lrest, rrest-1)
        backtrack('', 0,0, n, n)
        return ans
# @lc code=end
