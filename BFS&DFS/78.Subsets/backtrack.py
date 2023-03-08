class Solution:
    def subsets(self, nums: list) -> list:
        n = len(nums)
        res = []

        def backtrack(i, tmp):
            res.append(tmp)
            for x in range(i, n):

                backtrack(x + 1, tmp + [nums[x]])
            return
        backtrack(0, [])
        return res


nums = [1, 2, 3]
a = Solution().subsets(nums)
print(a)
print(len(a) == 2 ** (len(nums)))