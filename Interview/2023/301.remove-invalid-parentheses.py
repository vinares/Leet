#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> list:
        res = set()
        # quota for removal
        left, right = 0, 0
        for x in s:
            if x == '(':
                left += 1
            elif x == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        def dfs(left, right, i, leftres,rightres, tmp):
            if i == len(s):
                if left == 0 and right == 0:
                    res.add(tmp)
                return
            
            # skip () by using quota
            if s[i] == '(' and left > 0:
                dfs(left - 1, right,i+1,leftres,rightres,tmp)
            if s[i] == ')' and right > 0:
                dfs(left,right - 1,i + 1,leftres,rightres,tmp)
            # add alphabetic char
            # add more ( is safe. In the end, quota remains and we don't adopt them.
            # only when there are more (, we can add ). This ensures validity
            if s[i] not in '()':
                dfs(left,right,i+1,leftres,rightres,tmp+s[i])
            elif s[i] == '(':
                dfs(left, right,i+1,leftres + 1,rightres,tmp+s[i])
            elif leftres > rightres:
                dfs(left, right, i+1, leftres,rightres + 1,tmp + s[i])

            return

        dfs(left,right,0,0,0,'')
        return list(res)

# @lc code=end

