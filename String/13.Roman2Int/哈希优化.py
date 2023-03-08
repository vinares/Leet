class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans, i, n = 0, 0, len(s)

        while n - i:
            if i == len(s) - 1:
                ans += dictionary[s[i]]
                i += 1
            else:
                if dictionary[s[i + 1]] > dictionary[s[i]]:
                    ans += dictionary[s[i + 1]] - dictionary[s[i]]
                    i += 2
                else:
                    ans += dictionary[s[i]]
                    i += 1

        return ans

print(Solution().romanToInt(s= "MCMXCIV"))

