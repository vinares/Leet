class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
        bucket = dict()
        for i in range(len(nums)):
            nth = nums[i] // (t + 1)
            if nth in bucket:
                return True
            if nth - 1 in bucket and abs(bucket[nth - 1] - nums[i]) <= t:
                return True
            if nth + 1 in bucket and abs(bucket[nth + 1] - nums[i]) <= t:
                return True
            bucket[nth] = nums[i]
            if i >= k:
                bucket.pop(nums[i - k] // (t + 1))
        return False
nums = [1,0,1,1]
print(Solution().containsNearbyAlmostDuplicate(nums,1,2))