class Solution:
    def removeDuplicates(self, nums: list) -> int:
        n = len(nums)
        j,  cnt= 1, 1
        i = 1
        while i < n:
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                nums[j] = nums[i]
                j += 1
                i += 1
            else:
                i += 1
        return j

case = Solution()
nums = [1,1,1,2,2,3]
print(case.removeDuplicates(nums))