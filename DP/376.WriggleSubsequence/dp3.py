class Solution:
    def wiggleMaxLength(self, nums: list) -> int:
        if not nums: return 0
        n = len(nums)
        up = None       # flag -- 'Should go up'
        length = 1
        for i in range(1, n):
            if nums[i] > nums[i-1] and up != True:
                length +=1
                up = True
            if nums[i] < nums[i-1] and up != False:
                length += 1
                up = False
        return length

nums = [1, 7, 4, 9, 2, 5]
print(Solution().wiggleMaxLength(nums))