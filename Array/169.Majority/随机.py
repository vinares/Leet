import random
class Solution:
    def majorityElement(self, nums: list) -> int:
        n = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 if num == candidate else 0 for num in nums) > n:
                return candidate
nums = [3,2,3]
print(Solution().majorityElement(nums))
