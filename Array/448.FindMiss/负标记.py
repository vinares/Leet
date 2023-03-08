class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        n = len(nums)
        if not nums:
            return []
        result = []
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] < 0:
                continue
            else:
                nums[abs(num) - 1] *= -1
        for i, num in enumerate(nums):
            if num > 0:
                result.append(i + 1)
        return result
case = Solution()
nums = [4,3,2,7,8,2,3,1]
print(case.findDisappearedNumbers(nums))