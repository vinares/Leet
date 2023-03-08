class Solution:
    def search(self, nums: list, target: int)  -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

case = Solution()
print(case.search([-1,0,3,5,9,12], 12))
