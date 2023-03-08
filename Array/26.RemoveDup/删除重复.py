class Solution:
    def removeDuplicates(self, nums: list) -> int:
        n = len(nums)
        i, j= 0, 0
        while i < n - 1:
            cur, j = nums[i], j + 1
            if j > n + 1:
                break
            while j <= n - 1:
                if nums[j] == cur:
                    j += 1
                else:
                    nums[i + 1] = nums[j]
                    i += 1
                    break
        return i + 1

case = Solution()
nums = [0,0,1,1,1,1,2,3,3]
print(case.removeDuplicates(nums))