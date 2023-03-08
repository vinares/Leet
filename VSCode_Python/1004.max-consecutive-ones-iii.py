#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lsum, rsum = 0, 0
        left = 0
        ans = 0 
        for right in range(len(nums)):
            rsum += 1-nums[right]
            while lsum < rsum - k:
                lsum += 1-nums[left]
                left += 1
            ans = max(ans, right-left+1)
        return ans



# @lc code=end

