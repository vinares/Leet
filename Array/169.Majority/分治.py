class Solution:
    def majorityElement(self, nums: list) -> int:
        def devideAndConquer(lo, hi):
            if lo == hi:
                return nums[lo]
            mid = lo + (hi - lo) // 2
            left = devideAndConquer(lo, mid)
            right = devideAndConquer(mid + 1, hi)

            if left == right:
                return left

            leftcount = sum(1 for num in nums[lo: hi + 1] if num == left)
            rightcount = sum(1 for num in nums[lo: hi + 1] if num == right)

            return left if leftcount > rightcount else right
        return devideAndConquer(0, len(nums) - 1)

nums = [3,2,3]
print(Solution().majorityElement(nums))
