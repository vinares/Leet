import math


class Solution:
    def factorCombinations(self, n):

        res = []
        def dfs(tmp, rest):
            if rest == 1:
                res.append(tmp[:])
                return
            cur = tmp[-1] if tmp else 2
            for i in range(cur, rest + 1):
                if rest % i == 0:
                    dfs(tmp + [i], rest // i)
        dfs([], n)
        res.pop()
        return res


print(Solution().factorCombinations(12))