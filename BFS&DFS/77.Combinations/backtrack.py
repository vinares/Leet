class Solution:
    def combine(self, n: int, k: int) -> list:
        if k > n:
            return []
        res = []
        def backtrack(i, tmp):
            if len(tmp)==k:
                res.append(tmp)
            for j in range(i, n + 1):
                backtrack(j + 1, tmp + [j])

        backtrack(1, [])
        return res

print(Solution().combine(4,2))
