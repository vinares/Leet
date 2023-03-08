#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ans = 0

        def backtrack(i, val):
            if i== len(nums):
                if val == target:
                    self.ans += 1
                return
            backtrack(i+1, val + nums[i])
            backtrack(i+1, val - nums[i])
            return
        
        backtrack(0, 0)
        return self.ans

# @lc code=end

