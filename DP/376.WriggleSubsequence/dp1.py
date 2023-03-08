class Solution:
    def wiggleMaxLength(self, nums: list) -> int:
        n = len(nums)
        if n < 1: return 0
        if n == 1: return 1

        ups = [[nums[i]] for i in range(n)]
        downs = [[nums[i]] for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                if ups[j][-1] > nums[i] and len(ups[j]) >= len(downs[i]):
                    downs[i] = ups[j] + [nums[i]]
                if downs[j][-1] < nums[i] and len(downs[j]) >= len(ups[i]):
                    ups[i] = downs[j] + [nums[i]]
        ans = ups[0]
        for i in range(n):
            if len(ups[i]) > len(ans):
                ans = ups[i]
            if len(downs[i]) > len(ans):
                ans = downs[i]

        return  len(ans)
nums = [1, 7, 4, 9, 2, 5]
print(Solution().wiggleMaxLength(nums))