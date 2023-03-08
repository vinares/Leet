class Solution:
    def majorityElement(self, nums: list) -> int:
        from collections import Counter
        dictionary = Counter(nums)
        print(dictionary)
        for num, time in dictionary.items():
            if time > len(nums) // 2:
                return num

nums = [3,2,3]
print(Solution().majorityElement(nums))
