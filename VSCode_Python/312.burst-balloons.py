#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, iNums):
        if not iNums: return 0
        nums = [1] + iNums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for i in range(n)]
        for i in range(2, n):
            for left in range(0, n-i):
                right = left + i
                for mid in range(left+1, right):
                    dp[left][right] = max(dp[left][right], nums[left]*nums[mid]*nums[right]+
                        dp[left][mid]+dp[mid][right])
        for p in dp:
            print(p)
        return dp[0][n-1]
        

# @lc code=end

