class Solution:
    def grayCode(self, n: int) -> list:
        ans = [i for i in range(2 ** n)]
        for j in range(len(ans)):
            grey = bin(ans[j])
            ans[j] = int(grey[2])
            for i in range(3, len(grey)):
                high, low = int(grey[i - 1]), int(grey[i])
                ans[j] = ans[j] * 2 + (high ^ low)

        return ans

print(Solution().grayCode(n= 4))