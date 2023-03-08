class Solution:
    def combinationSum3(self, k: int, n: int) -> list:
        res = []
        def backtrack(tmp, next_val, rest):
            if rest < 0:
                return
            if len(tmp) == k and rest == 0:
                res.append(tmp[:])
                return
            for j in range(next_val, 10):
                if tmp and tmp[-1] >= j:continue
                backtrack(tmp + [j], next_val + 1, rest - j)

        backtrack([], 1, n)
        return res

print(Solution().combinationSum3(3, 9))