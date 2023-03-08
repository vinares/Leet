#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        cur_one = 0
        for num in nums:
            if num == 1:
                cur_one += 1
                max_one = max(max_one, cur_one)
            else:
                cur_one = 0
        return max_one

# @lc code=end

