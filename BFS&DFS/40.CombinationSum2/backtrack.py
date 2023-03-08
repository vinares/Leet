class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        res = []
        candidates.sort()
        path = []

        def backtrack(rest, i):
            if rest < 0:return
            if rest == 0:
                res.append(path[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]: continue
                if rest < candidates[i]:return
                path.append(candidates[j])
                backtrack(rest - candidates[j], j + 1)
                path.pop()

        backtrack(target, 0)
        return res


candidates = [10,1,2,7,6,1,5]

target = 8
a = Solution().combinationSum2(candidates,target)
print(a)