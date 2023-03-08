class Solution:
    def findUnsortedSubarray(self, nums: list) -> int:
        n = len(nums)
        mini, maxi = n - 1, 0
        left, right = n - 1, 0
        for i in range(1,n):
            if nums[i] < nums[i - 1]:
                mini = i if nums[i] < nums[mini] else mini
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                maxi =  i if nums[i] > nums[maxi] else maxi

        for i in range(n):
            if nums[i] > nums[mini]:
                left = min(left, i)
        for i in range(n - 1, -1, -1):
            if nums[i] < nums[maxi]:
                right = max(right, i)
        return right - left + 1 if right > left else 0

case = Solution()
nums =  [1,3,2,3,3]
print(case.findUnsortedSubarray(nums))