class Solution:
    def canPartition(self, nums: list) -> bool:
        sum, n = 0, len(nums)
        for num in nums:
            sum += num
        if sum % 2:
            return False
        sum //= 2
        dp = [-sum] * (n + 1)
        for i, num in enumerate(nums):
            tmp = list(dp)
            for j in range(1, i + 2):
                print(dp)
                if tmp[j - 1] + num > 0:
                    continue
                elif tmp[j - 1] + num < 0:
                    dp[j] = max(dp[j], tmp[j - 1] + num)
                else:
                    return True
        return False



print(Solution().canPartition(nums=[23,13,11,7,6,5,5]))