class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m <= n / 2:
            return 0
        ans = 2 ** 32 - 1
        for i in range(m, n + 1):
            ans &= i
        return ans



print(Solution().rangeBitwiseAnd(5,7))