class Solution:
    def rotate(self, nums: list, k: int) -> None:
        n = len(nums)
        k %= n
        if k < n / 2:
            tmp = nums[n - k: n].copy()
            for i in range(n - 1, k - 1, -1):
                nums[i] = nums[i - k]
            for i in range(k):
                nums[i] = tmp[i]
        else:
            tmp = nums[0: n - k].copy()
            for i in range(k):
                nums[i] = nums[i + n - k]
            for i in range(k, n):
                nums[i] = tmp[i - k]




case = Solution()
nums =  [1,2,3,4,5,6,7]
case.rotate(nums, 6)
print(nums)