#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        if j == 0:
            return 0
        sorted_nums = sorted(nums)
        while i<len(nums) and sorted_nums[i] == nums[i]:
            i += 1
        while j>=0 and sorted_nums[j] == nums[j]:
            j -= 1
        return max(0, j-i+1)


# @lc code=end

