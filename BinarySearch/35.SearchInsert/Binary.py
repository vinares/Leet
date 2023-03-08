class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] > target:
            return 0
        if nums[right] < target:
            return (right + 1)
        while left <= right:
            mid = left + (right - left)//2
            print(left)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

case = Solution()
print(case.searchInsert([1,3,5,6],2))