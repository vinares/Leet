class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:return True
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n - i - 1]:
                return s[i+1:n - i] == s[i+1:n - i][::-1] or s[i:n-1-i] == s[i:n-1-i][::-1]
        return True



s = "abdfca"
print(Solution().validPalindrome(s))