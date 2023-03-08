class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for x in s:
            ans *= 26
            ans = ans + ord(x) - ord('A') + 1
        return ans

print(Solution().titleToNumber(s='AA'))