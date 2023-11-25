class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        ans = []

        def backtrack(nums, i, tmp):
            if i >= len(nums) or sum(tmp) > target or len(tmp) > 150: return
            if sum(tmp) == target:
                ans.append(tmp)

            for index in range(i, len(nums)):
                if nums[index] > target - sum(tmp): break
                backtrack(nums, index, tmp + [nums[index]])
            return
        candidates = sorted(set(candidates))
        backtrack(candidates, 0, [])
        return ans

candidates = [2,2,2,4]
target = 8
print(Solution().combinationSum(candidates, target))