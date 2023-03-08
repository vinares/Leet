from math import comb
class Solution:
    def getRow(self, numRows: int) -> list:
        return [comb(numRows, i) for i in range(numRows+1)]
print(Solution().getRow(31))