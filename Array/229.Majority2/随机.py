class Solution:
    def majorityElement(self, nums: list) -> int:
        import random
        ans = []

        for i in range(len(nums) * 8):
            if len(ans) == 2: break
            candidate = random.choice(nums)
            if sum(1 for i, num in enumerate(nums) if num == candidate) > len(nums) / 3:
                ans.append(candidate)
            if len(ans) == 2 and ans[1] == ans[0]:
                ans.pop()
        return ans

nums = [3,2,3]
print(Solution().majorityElement(nums))
