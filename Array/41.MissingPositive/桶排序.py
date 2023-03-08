class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return n + 1

nums = [-10,-3,-100,-1000,-239,1]
print(Solution().firstMissingPositive(nums))