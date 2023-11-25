#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return n-1
        l, r = 0, n -1 
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m] <= nums[m-1]:
                r = m
            else:
                l = m+1
        print(l, r)
        return r if nums[r] > nums[l] else l
# @lc code=end

