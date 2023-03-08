#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left_brackets, right_brackets = 0, 0
        self.ans = set()
        for c in s:
            if c == '(':
                left_brackets += 1
            elif c == ')':
                if left_brackets > 0:
                    left_brackets -= 1
                else:
                    right_brackets += 1
            
        def backtrack(index, expr, left_brackets, right_brackets, left_in_expr, right_in_expr):
            if index == len(s): 
                if left_brackets == 0 and right_brackets == 0:
                    self.ans.add(''.join(expr))
                return

            if s[index] == '(' and left_brackets > 0:
                backtrack(index+1, expr, left_brackets-1, right_brackets, left_in_expr, right_in_expr)
            if s[index] == ')' and right_brackets > 0:
                backtrack(index+1, expr, left_brackets, right_brackets-1, left_in_expr, right_in_expr)
            
            if s[index] not in '()':
                backtrack(index+1, expr+[s[index]], left_brackets, right_brackets, left_in_expr, right_in_expr)
            elif s[index] == '(':
                backtrack(index+1, expr+[s[index]], left_brackets, right_brackets, left_in_expr+1, right_in_expr)
            elif left_in_expr > right_in_expr:
                backtrack(index+1, expr+[s[index]], left_brackets, right_brackets, left_in_expr, right_in_expr+1)
            return
        
        backtrack(0, [], left_brackets, right_brackets, 0, 0)
        return list(self.ans) 



# @lc code=end

