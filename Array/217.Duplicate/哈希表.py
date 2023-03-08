class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        check = set(nums)
        if len(check) < len(nums):
            return True
        else:
            return False

nums = [1,2,3,1]
print(Solution().containsDuplicate(nums))