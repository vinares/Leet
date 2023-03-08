class Solution:
    def search(self, nums: list) -> int:
        left, right = 0, len(nums) - 1
        if not nums:
            return -1
        while left < right:
            mid = (right + left)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
case = Solution()
print(case.search([3,4,0,1,2]))