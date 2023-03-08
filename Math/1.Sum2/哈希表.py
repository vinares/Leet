class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        n = len(nums)
        a = dict()
        for i in range(n):
            if (target - nums[i]) in a:
                return [a[target - nums[i]], i]
            a[nums[i]] = i
        return []

case = Solution()
nums = [2,7,11,15]
target = 9
print(case.twoSum(nums, target))