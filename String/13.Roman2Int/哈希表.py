class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        ans, cur, i = 0, '', 0

        while len(s) - i:
            if len(s) > i + 1 and s[i] + s[i + 1] in dictionary:
                ans += dictionary[s[i] + s[i + 1]]
                i += 2
            else:
                ans += dictionary[s[i]]
                i += 1
        return ans

print(Solution().romanToInt(s= "MCMXCIV"))

