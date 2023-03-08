class Solution:
    def majorityElement(self, nums: list) -> int:
        count, candidate = 0, nums[0]
        for i, num in enumerate(nums):
            if num == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = num
                count += 1
        return candidate

nums = [3,2,3]
print(Solution().majorityElement(nums))
