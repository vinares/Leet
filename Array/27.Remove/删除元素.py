class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j

case = Solution()
nums = [3,2,2,3]
print(case.removeElement(nums, 3))