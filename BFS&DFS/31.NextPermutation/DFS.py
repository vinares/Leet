class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if not i:break
            if nums[i] > nums[i - 1]:
                for j in range(n - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        nums[i-1], nums[j] = nums[j], nums[i - 1]
                        break
                break

        left, right = i, n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums



nums = [1,1,5]
print(Solution().nextPermutation(nums))