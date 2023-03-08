class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n == 1: return nums
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]: break
            i -= 1
        if i == -1:
            for j in range(n // 2):
                nums[j], nums[n - j - 1] = nums[n - j - 1], nums[j]
            return nums

        j = n - 1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1::] = nums[i + 1::][::-1]
        return nums