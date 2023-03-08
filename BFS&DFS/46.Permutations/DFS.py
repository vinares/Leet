class Solution:
    def permute(self, nums: list) -> list:
        res = []
        def dfs(start=0):
            if start == len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        dfs()

        return res



nums = [1,2,3]
print(Solution().permute(nums))