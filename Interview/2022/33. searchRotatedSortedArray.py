class Solution:
    def search(self, nums: list, target: int) -> int:
        l, r = 0, len(nums)
        while l <= r:
            m = l + (r - l)//2
            if nums[m] == target: return m
            if target >= nums[0]:
                if nums[m] < nums[0]:
                    r = m - 1
                elif nums[m] > target:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] > nums[0]:
                    l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r -= 1
        if nums[l] != target: return -1
        return l

nums = [4,5,6,7,0,1,2]
target = 0
print(Solution().search(nums,target))