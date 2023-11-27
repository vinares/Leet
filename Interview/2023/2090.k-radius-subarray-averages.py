#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        if 2*k + 1 > n: 
            return ans
        k_sum = sum(nums[:2*k+1])
        left, right, mid = 0, 2*k, k
        ans[mid] = k_sum//(2*k+1)
        right += 1
        while right < n:
            mid += 1
            k_sum += (nums[right] - nums[left])
            ans[mid] = k_sum // (2*k + 1)
            left += 1
            right += 1
        return ans
            


# @lc code=end

