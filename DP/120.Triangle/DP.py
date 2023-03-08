class Solution:
    def minimumTotal(self, triangle: list) -> int:
        n = len(triangle)
        if not n: return 0

        m = len(triangle[-1])
        dp = [0 for _ in range(m)]
        dp[0] = triangle[0][0]
        for i in range(1, n):
            bucket = dp.copy()
            dp[0] = bucket[0] + triangle[i][0]
            for j in range(1, i):
                dp[j] = min(bucket[j - 1] , bucket[j]) + triangle[i][j]
            dp[i] = bucket[i-1] + triangle[i][i]
        return min(dp)

print(Solution().minimumTotal(triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]))