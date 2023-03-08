class Solution:
    def majorityElement(self, nums: list) -> int:
        from collections import Counter
        ans = []
        for num, time in Counter(nums).items():
            if time > len(nums) // 3:
                ans.append(num)
        return ans

nums = [3,2,3]
print(Solution().majorityElement(nums))
