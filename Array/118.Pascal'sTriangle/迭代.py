class Solution:
    def generate(self, numRows: int) -> list:
        if not numRows: return[]
        ans = []
        for i in range( numRows):
            ans.append([1] * (i + 1))
            for j in range(1, i//2 + 1):
                tmp = ans[i - 1][j - 1] + ans[i - 1][j]
                ans[i][j], ans[i][i - j] = tmp, tmp
        return ans


print(Solution().generate(5))