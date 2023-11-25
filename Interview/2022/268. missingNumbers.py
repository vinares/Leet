class Solution:
    def missingNumber(self, nums: list) -> int:
        for i in range(len(nums)):
            while i != nums[i] != len(nums):
                num = nums[i]
                nums[num], nums[i] = nums[i], nums[num]


        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

nums = [1, 2, 0]
print(Solution().missingNumber(nums))