class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n &= n - 1
        return n


print(Solution().rangeBitwiseAnd(5,7))