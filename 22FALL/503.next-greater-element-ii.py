#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        n = len(nums)
        stack = []
        for i in range(2*n-1):
            while stack and nums[stack[-1]] < nums[i%n]:
                ans[stack.pop()] = nums[i%n]
            stack.append(i%n)
        return ans


# @lc code=end

