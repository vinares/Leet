class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)



nums =  [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))