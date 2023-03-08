class Solution:
    def removeInvalidParentheses(self, s: str) -> list:
        res = set()
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

            if s[i] == '(' and left > 0:
                dfs(left - 1, right,i+1,leftres,rightres,tmp)
            if s[i] == ')' and right > 0:
                dfs(left,right - 1,i + 1,leftres,rightres,tmp)

            if s[i] not in '()':
                dfs(left,right,i+1,leftres,rightres,tmp+s[i])
            elif s[i] == '(':
                dfs(left, right,i+1,leftres + 1,rightres,tmp+s[i])
            elif leftres > rightres:
                dfs(left, right, i+1, leftres,rightres + 1,tmp + s[i])

            return

        dfs(left,right,0,0,0,'')
        return list(res)


s = "(a)())()"
print(Solution().removeInvalidParentheses(s))