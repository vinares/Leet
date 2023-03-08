class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, min(len(nums), k + i + 1)):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

nums = [1,0,1,1]
print(Solution().containsNearbyAlmostDuplicate(nums,1,2))