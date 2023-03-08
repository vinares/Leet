class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        invalid = []
        slist = list(s)
        for i in range(len(s)):
            if s[i] not in '()':continue
            elif s[i] == ')' and invalid and s[invalid[-1]] == '(': invalid.pop()
            else : invalid.append(i)
        while invalid:
            slist[invalid.pop()] = ''
        return ''.join(slist)


s = "lee(t(c)o)de)"
print(Solution().minRemoveToMakeValid(s))