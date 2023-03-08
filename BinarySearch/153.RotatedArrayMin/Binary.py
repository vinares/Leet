class Solution:
    def search(self, nums: list) -> int:
        left, right = 0, len(nums) - 1
        if not nums:
            return -1
        while left <= right:
            mid = (right + left)//2
            if nums[left] <= nums[right]:
                return nums[left]
            elif nums[left] <= nums[mid]:
                if nums[left] >= nums[right]:
                    left = mid + 1
                else:
                    return nums[left]
            else:
                if nums[mid] >= nums[mid - 1]:
                    right = mid - 1
                else:
                    return nums[mid]
        return nums[left]
case = Solution()
print(case.search([3,4,0,1,2]))


