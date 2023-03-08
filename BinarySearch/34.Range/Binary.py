class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        left, right = 0, len(nums) -1
        if not nums:
            return [-1, -1]
        if nums[right] == target:
            r = right
        else:
            while left < right:
                mid = left + (right - left) // 2 + 1
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            if nums[left] == target:
                r = left
            else:
                return [-1,-1]

        left, right = 0, len(nums) - 1

        if nums[left] == target:
            l = left
        else:
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            if nums[right] == target:
                l = right
            else:
                return [-1, -1]

        return [l, r]

import time
t = time.monotonic()
case = Solution()
print(case.searchRange([1,2,45], 3))
print(time.monotonic()-t)
