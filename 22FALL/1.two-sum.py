#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            if target -  nums[i] in nums[i+1:len(nums)]:
                return [i, nums[i+1:len(nums)].index(target - nums[i])]

# @lc code=end

