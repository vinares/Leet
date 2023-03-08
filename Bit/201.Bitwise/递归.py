class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        import math
        def recurse(m, n):
            if not m or not n:
                return 0
            if m >= n:
                return m
            exp = int(math.log(n, 2))
            if int(math.log(m, 2)) < exp:
                return 0
            ans = 2 ** exp
            return ans + recurse(m - ans, n - ans)
        return recurse(m, n)

print(Solution().rangeBitwiseAnd(3,4))