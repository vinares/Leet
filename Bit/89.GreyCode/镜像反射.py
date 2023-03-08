class Solution:
    def grayCode(self, n: int) -> list:
        ans = [0]
        for ith in range(1, n + 1):
            last = 2 ** (ith - 1)
            for i in range(last, 2 ** ith):
                if i > 2 ** n:
                    break
                ans.append(last + ans[2 * last - i - 1])

        return ans



print(Solution().grayCode(n= 4))