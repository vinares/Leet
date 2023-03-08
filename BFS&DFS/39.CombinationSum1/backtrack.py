class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        res = []
        n = len(candidates)
        def backtrack(i, tmp, rest):
            if rest < 0:
                return 
            if rest == 0:
                res.append(tmp)
                return
            for j in range(i, n):
                if candidates[j] <= rest:
                    backtrack(j, tmp + [candidates[j]], rest - candidates[j])

        backtrack(0,[],target)
        return res


candidates = [2, 3, 6, 7]
target = 7

a = Solution().combinationSum2(candidates,target)
print(a)