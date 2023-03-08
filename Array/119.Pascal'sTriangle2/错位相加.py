class Solution:
    def getRow(self, numRows: int) -> list:
        if not numRows + 1: return[]
        ans = [[1]]
        for i in range(1, numRows + 1):
            newrow = [j + k for j, k in zip(ans[-1] + [0], [0] + ans[-1])]
            ans.append(newrow)
        return ans[-1]

print(Solution().getRow(4))