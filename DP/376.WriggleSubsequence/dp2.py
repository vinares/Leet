class Solution:
    def wiggleMaxLength(self, nums: list) -> int:
        n = len(nums)
        if n < 1: return 0
        if n == 1: return 1

        ups = [1 for i in range(n)]
        downs = [1 for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[j] > nums[i] and ups[j] >= downs[i]:
                    downs[i] = ups[j] + 1
                if nums[j] < nums[i] and downs[j] >= ups[i]:
                    ups[i] = downs[j]+1
        end = 0

        for i in range(n):
            if ups[i] > end:
                end = ups[i]
            if downs[i] > end:
                end = downs[i]

        return  end
nums = [1, 7, 4, 9, 2, 5]
print(Solution().wiggleMaxLength(nums))