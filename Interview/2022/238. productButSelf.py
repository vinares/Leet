class Solution:
    def productExceptSelf(self, nums: list) -> list:
        n = len(nums)
        ans = [1 for _ in range(n)]
        lp = 1
        for i in range(n):
            ans[i] = lp
            lp *= nums[i]
        rp = 1
        for i in reversed(range(n)):
            ans[i] *= rp
            rp *= nums[i]
        return ans


nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))