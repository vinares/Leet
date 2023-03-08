class Solution:
    def numSquares(self, n: int) -> int:
        squarenum = set([(i + 1) ** 2 for i in range(round(n ** 0.5))])
        def divide_by(m:int, count: int) -> bool:
            if count== 1:
                return m in squarenum

            for num in squarenum:
                if divide_by(m - num, count - 1):
                    return True
            return False


        for i in range(1, n + 1):
            if divide_by(n, i):
                return i

print(Solution().numSquares(23146954734456))