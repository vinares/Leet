class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        positive = set()
        for i, num in enumerate(nums):
            if num > 0:
                positive.add(num)
        if not positive: return 1
        positive = list(positive)
        positive.sort()
        if positive[0] > 1: return 1
        count = positive[0]
        for i in range(1, len(positive)):
            if positive[i] != i + 1:
                return i + 1
        return len(positive) + 1


nums = [1,2,2,1,0]
print(Solution().firstMissingPositive(nums))