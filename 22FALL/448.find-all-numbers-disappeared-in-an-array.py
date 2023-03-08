#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for _ in range(n)]
        for num in nums:
            ans[num-1] += 1
        return [i+1 for i in range(n) if ans[i] == 0]

# @lc code=end

