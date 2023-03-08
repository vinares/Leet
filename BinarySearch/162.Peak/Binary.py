class Solution:
    def findPeakElement(self, nums: list) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] < nums[mid + 1]: left = mid + 1
            else: right = mid
        return right
case = Solution()
print(case.findPeakElement([1,0,0,0,0,0]))