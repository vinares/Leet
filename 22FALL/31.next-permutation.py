#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bigger = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i == 0:
                nums.sort()
                return
            if nums[i] > nums[i - 1]:
                bigger = i - 1
                break
        for j in range(len(nums) - 1, bigger, -1):
            if nums[j] > nums[bigger]:
                nums[j], nums[bigger] = nums[bigger], nums[j]
                break
        nums[bigger+1::] = sorted(nums[bigger+1::])
        
# @lc code=end
