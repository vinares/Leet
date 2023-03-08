from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(maxsize=128)
        def match(s, p, prev):

            ans = False
            if s and s[0] == prev:
                ans = ans or match(s[1:], p, prev)

            if s == '':
                return True
            if s == '' or p == '':
                return ans
            if len(p) >= 2 and p[0:2] == '.*':
                return True
            if s[0] == p[0] or p[0] == '.':
                if len(p) >= 2 and p[1] == '*':
                    ans = ans or match(s[1:], p[2:], s[0])
                    ans = ans or match(s, p[2:], '')
                ans = ans or match(s[1:], p[1:], '')
            else:
                if len(p)>=2 and p[1] =='*':
                    ans = ans or match(s, p[2:], '')
            return  ans

        return match(s, p, '')

s = 'aab'
p = 'c*a*b'
print(Solution().isMatch(s, p))
