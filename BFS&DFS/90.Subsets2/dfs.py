class Solution:
    def subsetsWithDup(self, nums: list) -> list:
        res = []
        nums.sort()
        def backtrack(tmp, i):
            res.append(tmp)
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:continue
                backtrack(tmp + [nums[j]], j + 1)
        backtrack([], 0)
        return res

nums = [4,4,4,1,4]
print(Solution().subsetsWithDup(nums))