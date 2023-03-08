class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        while n:
            ans = chr(ord('A') + (n - 1) % 26) + ans
            n = (n - 1) // 26
        return ans


print(Solution().convertToTitle(28))