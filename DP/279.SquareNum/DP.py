class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n for _ in range(n + 1)]
        square_num = [i ** 2 for i in range(1, round(n ** 0.5) + 1)]
        id = 0
        for i in range(1, n + 1):
            if id < len(square_num) and i == square_num[id]:
                id += 1
                dp[i] = 1
                continue

            for j in range(id):
                dp[i] = min(dp[i], 1 + dp[i - square_num[j]])
        return dp[n]




print(Solution().numSquares(1111))