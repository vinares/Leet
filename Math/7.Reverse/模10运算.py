class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        boundry = (1 << 31) if x >= 0 else (1 << 31) - 1
        while y:
            res =  res * 10 + y % 10
            y //= 10
            if res > boundry:
                return 0
        return res if x >= 0 else - res

case = Solution()
print(case.reverse(-901000))