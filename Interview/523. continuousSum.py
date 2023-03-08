class Solution:
    def checkSubarraySum(self, nums: list, target: int) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            if nums[0] == target: return True
            return False
        if nums[0] == target: return True
        s = nums[0] + nums[1]
        i, j = 0, 1

        while i < len(nums) and j < len(nums):
            if s == target:
                return True
            elif s > target:
                s -= nums[i]
                i += 1
                if s <= 0 and i < len(nums):
                    s = nums[i]
                    j += 2
            else:
                j += 1
                if j >= len(nums): return False
                s += nums[j]
        return s == target

print(Solution().checkSubarraySum([1,2,3,4,5,6,7,8,9], 6))