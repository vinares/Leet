class Solution:
    def jump(self, nums: list) -> int:
        furthest, cur, step, n = 0, 0, 0, len(nums)
        for i in range(n):
            if cur >= n - 1:
                return step
            if furthest >= i:
                furthest = max(furthest, i + nums[i])
                if i == cur:
                    cur = furthest
                    step += 1
        return step


nums = [2,3,1,1,4]
print(Solution().jump(nums))