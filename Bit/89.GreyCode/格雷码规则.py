class Solution:
    def grayCode(self, n: int) -> list:
        ans = [0]
        for ith in range(1, 2 ** n):
            previous = ans[ith - 1]
            if ith % 2 == 1:
                ans.append(previous ^ 1)
            else:
                a = (previous & ( -previous)) << 1
                ans.append(a ^ previous)
        return ans


print(Solution().grayCode(n= 4))