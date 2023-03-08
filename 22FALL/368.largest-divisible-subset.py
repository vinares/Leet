#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        mem = [[nums[i]] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(mem[j]) >= len(mem[i]):
                    mem[i] = mem[j] + [nums[i]]
        return sorted(mem, key=lambda x: len(x), reverse=True)[0]
# @lc code=end

