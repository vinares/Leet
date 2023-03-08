class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        n = len(nums)
        if not n: return 1
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = n + 1
        for i, num in enumerate(nums):
            if abs(num) <= n:
                nums[abs(num) - 1] = - abs(nums[abs(num) - 1])
        for i, num in enumerate(nums):
            if num > 0:
                return i + 1
        return n + 1


nums = [1]
print(Solution().firstMissingPositive(nums))