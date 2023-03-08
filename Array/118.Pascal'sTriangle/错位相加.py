class Solution:
    def generate(self, numRows: int) -> list:
        if not numRows: return[]
        ans = [[1]]
        for i in range(1, numRows):
            newrow = [j + k for j, k in zip(ans[-1] + [0], [0] + ans[-1])]
            ans.append(newrow)
        return ans


print(Solution().generate(5))