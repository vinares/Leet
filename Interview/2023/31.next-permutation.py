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
        def reverse(nums, start):
            #start included
            end = len(nums)-1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            
        start = len(nums) - 2
        while start >= 0 and nums[start] >= nums[start+1]:
            start -= 1
        if start >= 0:
            for i in range(len(nums)-1, start, -1):
                if nums[i] > nums[start]:
                    nums[i], nums[start] = nums[start], nums[i]
                    break
        reverse(nums, start+1)
     
# @lc code=end

