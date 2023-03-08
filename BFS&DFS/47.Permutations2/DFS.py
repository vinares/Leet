class Solution:
    def permuteUnique(self, nums: list) -> list:
        res = []
        nums.sort()
        def backtrack(tmp, nums):
            if not nums:
                res.append(tmp)
            for i in range(len(nums)):
                if i != 0 and nums[i] == nums[i - 1]: continue
                backtrack(tmp + [nums[i]], nums[0:i] + nums[i + 1:])
        backtrack([], nums)
        return res


nums =  [1,1,2]
print(Solution().permuteUnique(nums))