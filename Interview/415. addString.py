class Solution:
    def addStrings(self, s: str, t: str) -> str:
        i, j = len(s) - 1, len(t) - 1
        carry = False
        ans = ''

        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                cur = int(s[i]) + int(t[j])
                i -= 1
                j -= 1
            elif i < 0:
                cur = int(t[j])
                j -= 1
            else:
                cur = int(s[i])
                i -= 1

            if carry:
                carry = False
                cur += 1
            ans += str(cur % 10)
            if cur > 10:
                carry = True

        if carry:
            ans += '1'
        return ans[::-1]

print(Solution().addStrings(s='1', t='9'))