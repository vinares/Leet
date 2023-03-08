class Solution:
    def rotate(self, nums: list, k: int) -> None:
        n = len(nums)
        k %= n
        def reverse(start, end):
            nums[start: end + 1] = nums[start:end+1][::-1]

        reverse(0,n - 1)
        reverse(0,k-1)
        reverse(k,n-1)
case = Solution()
nums =  [1,2,3,4,5,6,7]
case.rotate(nums, 6)
print(nums)