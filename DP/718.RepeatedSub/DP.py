class Solution:
    def findLength(self, A: list, B: list) -> int:
        a, b = len(A), len(B)
        dp = [[0] * (1 + a) for _ in range(1 + b)]
        ans = 0
        for i in range(a - 1, -1, -1):
            for j in range(b - 1, -1, -1):
                if i == a or j == b:
                    break
                if A[i] == B[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
            ans = max(max(dp[i]), ans)
        return ans



print(Solution().findLength(A=[1,2,3,2,1], B=[3,2,1,4,7]))