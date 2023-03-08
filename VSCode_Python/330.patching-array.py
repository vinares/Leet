#
# @lc app=leetcode id=330 lang=python3
#
# [330] Patching Array
#

# @lc code=start
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans, x = 0, 1
        index = 0

        while x <= n:
            if index < len(nums) and x >= nums[index]:
                x += nums[index]
                index += 1
            else:
                x <<= 1
                ans += 1
        return ans

# @lc code=end

