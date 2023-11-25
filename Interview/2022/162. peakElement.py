class Solution:
    def findPeakElement(self, nums: list) -> int:
        n = len(nums)
        if n == 0: return -1
        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2
            if m > l and nums[m] < nums[m - 1]: r = m - 1
            elif m < r and nums[m] < nums[m + 1]: l = m + 1
            else: return m
    def findLocalMinimum(self, nums):
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if mid < right and nums[mid] > nums[mid + 1]:
                left = mid + 1
            elif mid > left and nums[mid] > nums[mid - 1]:
                right = mid - 1
            else:
                return mid
        return mid

nums = [-1]
print(Solution().findPeakElement(nums))
print(Solution().findLocalMinimum(nums))